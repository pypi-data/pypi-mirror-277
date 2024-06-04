import asyncio
from loguru import logger
from dataclasses import dataclass, field

from cryptlab.common.broadcaster import AsyncEventBroadcaster, AsyncEventListener
from cryptlab.common.exceptions import InvalidRecipientError, PKIEntryAlreadySet
from cryptlab.common.messages import (
    ClosingOrchestrator,
    Event,
    EventQueueClosing,
    MessageQueue,
    NewServerScriptConnected,
    Message,
    ServerScriptConnectedEvent,
    ServerScriptDisconnectedEvent,
)

# TODO: cleaning up the mapping would not be terrible for memory efficiency...


class InvalidTokenError(Exception):
    pass


EventQueue = asyncio.Queue[Event]


@dataclass
class ServerScript:
    name: str
    orch_to_serv: MessageQueue


@dataclass
class BridgeEntry:
    server_id: str
    server_script: ServerScript | None = None
    event_broadcaster: AsyncEventBroadcaster = field(
        default_factory=AsyncEventBroadcaster
    )
    client_queues: dict[str, MessageQueue] = field(default_factory=dict)
    pki: dict[str, str] = field(default_factory=dict)

    async def send(self, client_id: str, message: Message):
        if client_id not in self.client_queues:
            raise InvalidRecipientError(
                f"Trying to send a message to {client_id}, which does not exist"
            )

        await self.client_queues[client_id].put(message)

    async def broadcast(self, event: Event):
        await self.event_broadcaster.broadcast(event)


class Bridge:
    def __init__(self):
        self.mappings: dict[str, BridgeEntry] = {}

    async def close(self):
        for entry in self.mappings.values():
            # Close all websockets
            await entry.event_broadcaster.broadcast(EventQueueClosing())

            # Close all TCP connections with server scripts
            server_script = entry.server_script
            if server_script:
                await server_script.orch_to_serv.put(ClosingOrchestrator())

    async def register_queue(
        self, server_id: str, name: str, orch_to_serv: MessageQueue
    ) -> None:
        match self.mappings.get(server_id):
            case None:
                # This happens when the client connects with a non-existing token
                raise InvalidTokenError(
                    f"Token {server_id} has not been previously registered"
                )
            case BridgeEntry(
                server_id, old_server_script, event_broadcaster, _
            ) as entry:
                if old_server_script is not None:
                    # There is another ServerScript connected, we should kill it
                    logger.debug(
                        "Killing existing ServerScript (name={}) for auth_code {}",
                        old_server_script.name,
                        server_id,
                    )
                    await old_server_script.orch_to_serv.put(NewServerScriptConnected())
                    await event_broadcaster.broadcast(
                        ServerScriptDisconnectedEvent(old_server_script.name)
                    )

                logger.debug(
                    "Registering new ServerScript for auth_code {} with name {}",
                    server_id,
                    name,
                )
                entry.server_script = ServerScript(name, orch_to_serv)
                await event_broadcaster.broadcast(ServerScriptConnectedEvent(name))
            case _:
                raise Exception("Should never happen")

    def is_server_script_connected(self, server_id: str) -> str | None:
        match self.mappings.get(server_id):
            case None:
                return None
            case BridgeEntry(_, server_script, _, _):
                if server_script is not None:
                    return server_script.name
                else:
                    return None
            case _:
                raise Exception("Should never happen")

    async def send_message(self, client_id: str, server_id: str, message: Message):
        if server_id not in self.mappings:
            raise InvalidTokenError(f"Server ID not valid {server_id}")
        await self.mappings[server_id].send(client_id, message)

    async def send_message_to_all_clients(self, server_id: str, message: Message):
        if server_id not in self.mappings:
            raise InvalidTokenError(f"Server ID not valid {server_id}")

        for queue in self.mappings[server_id].client_queues.values():
            await queue.put(message)

    async def clear_all_clients(self, server_id: str):
        if server_id not in self.mappings:
            # It might be that one connects with invalid server IDs, doesn't matter
            return

        self.mappings[server_id].client_queues = {}

    async def broadcast(self, server_id: str, event: Event):
        if server_id not in self.mappings:
            raise InvalidTokenError(f"Server ID not valid {server_id}")
        await self.mappings[server_id].broadcast(event)

    def register_token(self, server_id: str) -> None:
        match self.mappings.get(server_id):
            case None:
                logger.debug("Registered new token {}", server_id)
                self.mappings[server_id] = BridgeEntry(server_id)
            case BridgeEntry():
                # This would happen in case the auth code exists already
                # In this case, we do nothing
                pass
            case _:
                raise Exception("Should never happen")

    def register_listener(self, server_id: str, listener: AsyncEventListener):
        if server_id not in self.mappings:
            raise InvalidTokenError(f"Server ID not valid {server_id}")
        self.mappings[server_id].event_broadcaster.add_listener(listener)

    def get_orch_to_serv_queue(self, server_id: str) -> MessageQueue | None:
        if server_id not in self.mappings:
            return None

        entry = self.mappings[server_id]

        if entry.server_script is None:
            return None

        return entry.server_script.orch_to_serv

    def register_clients(self, server_id: str, client_queues: dict[str, MessageQueue]):
        if server_id not in self.mappings:
            raise InvalidTokenError(f"Server ID not valid {server_id}")

        self.mappings[server_id].client_queues |= client_queues

    def get_pki_entry(self, server_id: str, key: str) -> str | None:
        if server_id not in self.mappings:
            raise InvalidTokenError(f"Server ID not valid {server_id}")
        return self.mappings[server_id].pki.get(key, None)

    def set_pki_entry(self, server_id: str, key: str, value: str):
        if server_id not in self.mappings:
            raise InvalidTokenError(f"Server ID not valid {server_id}")

        if key in self.mappings[server_id].pki:
            raise PKIEntryAlreadySet()

        self.mappings[server_id].pki[key] = value
