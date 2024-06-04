import asyncio
import json
from cryptlab.common import cfg
from loguru import logger
from typing import Any

from cryptlab.common.exceptions import InvalidMessageError
from cryptlab.orchestrator.serverscripts.bridge import Bridge, InvalidTokenError
from cryptlab.common.messages import (
    ClosingOrchestrator,
    MessageQueue,
    NewServerScriptConnected,
    DataMessage,
    ServerDisconnected,
    ServerScriptDisconnectedEvent,
)
from cryptlab.common.utils import namegen

# A message is a dict that can be converted to JSON
# Note that JSON specifies that keys *must* be strings and will force
# them to be string if necessary.
Message = dict[str, Any]


class RequestHandler:
    def __init__(
        self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter, bridge: Bridge
    ):
        self.reader = reader
        self.writer = writer
        self.running = True
        self.bridge = bridge

    def stop(self):
        self.running = False

    async def read_message(self) -> Message:
        line = await self.reader.readline()
        return json.loads(line)

    async def send_message(self, obj: Message) -> None:
        msg = json.dumps(obj) + "\n"
        self.writer.write(msg.encode())
        await self.writer.drain()

    async def read_raw(self) -> bytes:
        return await self.reader.readline()

    async def send_raw(self, data: bytes) -> None:
        self.writer.write(data + b"\n")
        await self.writer.drain()

    async def on_new_connection(self):
        """Authenticate the ServerScript and establish connection"""
        auth_msg = await self.read_message()

        if "auth_code" not in auth_msg:
            await self.send_message({"error": "Missing authentication code"})
            return

        # TODO: change all instances of auth_code to server_script_id or smth like that
        server_id = auth_msg["auth_code"]

        await self.bridge.clear_all_clients(server_id)

        script_name = namegen.gen_random_name()
        orch_to_serv = MessageQueue()

        try:
            await self.bridge.register_queue(server_id, script_name, orch_to_serv)
        except InvalidTokenError:
            await self.send_message({"error": "Invalid code"})
            return

        # Start waiting now for actions from the clients and relay them to the server
        try:
            await self.send_message({"success": script_name})
            while True:
                try:
                    msg = await asyncio.wait_for(
                        orch_to_serv.get(), timeout=cfg.HEARTBEAT_TIMEOUT
                    )
                    match msg:
                        case NewServerScriptConnected():
                            # This ServerScript has been overridden by a new version
                            # so we can close the connection
                            break
                        case ClosingOrchestrator():
                            # Orchestrator is closing down... say goodbye!
                            break
                        case DataMessage(client_id, recipient_id, data):
                            # We can accept any client id, this should be handled at the application level
                            # We must, however, verify that the script id matches
                            if recipient_id != server_id:
                                raise InvalidMessageError(
                                    f"Received a message for {recipient_id}, but we are {server_id}"
                                )

                            await self.send_message(
                                {"client_id": client_id, "data": data}
                            )
                            response = await self.read_message()

                            if "client_id" not in response:
                                raise InvalidMessageError(
                                    f"Received a message without a recipient"
                                )

                            # TODO: for now we only require a single response from the server
                            # one day, it'd be nice to have a feature where the server can push arbitrary messages
                            # and clients have a "on_message" handler of some sort to simulate e.g. messaging apps?
                            # Sounds like a complicated feature to add though
                            if response["client_id"] != client_id:
                                raise InvalidMessageError(
                                    f"Received a message for {response['client_id']}, but server should be replying to {client_id}"
                                )

                            await self.bridge.send_message(
                                client_id,
                                server_id,
                                DataMessage(client_id, server_id, response["data"]),
                            )
                        case _:
                            raise Exception("Unexpected message")
                except TimeoutError:
                    # Check if the ServerScript is still alive
                    # We cannot always check if the TCP connection died on its own, but if the other side
                    # has disconnected cleanly, we expect an EOF from the reader

                    if not self.running or self.reader.at_eof():
                        await self.bridge.broadcast(
                            server_id, ServerScriptDisconnectedEvent(script_name)
                        )
                        break
        except Exception as e:
            logger.info("Request handler encountered an exception: {}", e)
            await self.bridge.broadcast(
                server_id, ServerScriptDisconnectedEvent(script_name)
            )
            await self.bridge.send_message_to_all_clients(
                server_id, ServerDisconnected()
            )


class TCPOrchestrator:
    def __init__(self, bridge: Bridge):
        self.handlers = set()
        self.bridge = bridge

    def stop_all_handlers(self):
        for handler in self.handlers:
            handler.stop()

    async def handle(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        handler = RequestHandler(reader, writer, self.bridge)
        self.handlers.add(handler)
        await handler.on_new_connection()
        writer.close()
        await writer.wait_closed()
