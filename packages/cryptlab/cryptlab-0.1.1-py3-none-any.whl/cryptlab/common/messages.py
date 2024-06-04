import asyncio
from dataclasses import dataclass
import json

# Messages for queues between (orchestrated) clients and orchestrator


class ClientDisconnected:
    client_id: str


class ServerDisconnected:
    pass


# Messages for queues between orchestrator and serverscript


@dataclass
class NewServerScriptConnected:
    pass


class ClosingOrchestrator:
    pass


# Messages for both queues


@dataclass
class DataMessage:
    client_id: str
    server_script_id: str
    data: dict


Message = (
    DataMessage
    | ClientDisconnected
    | ServerDisconnected
    | NewServerScriptConnected
    | ClosingOrchestrator
)
MessageQueue = asyncio.Queue[Message]

# Messages for event queue between orchestrator and web interface


@dataclass
class ServerScriptConnectedEvent:
    script_name: str

    def to_json(self) -> str:
        return json.dumps(
            {"event": "SERVER_SCRIPT_CONNECTED", "name": self.script_name}
        )


@dataclass
class ServerScriptDisconnectedEvent:
    script_name: str

    def to_json(self) -> str:
        return json.dumps(
            {"event": "SERVER_SCRIPT_DISCONNECTED", "name": self.script_name}
        )


class EventQueueClosing:
    def to_json(self) -> str:
        return json.dumps({"event": "EVENT_QUEUE_CLOSING"})


@dataclass
class NewClientsConnectedEvent:
    client_list: list[str]

    def to_json(self) -> str:
        return json.dumps({"event": "NEW_CLIENTS_CONNECTED", "list": self.client_list})


class ExecutionStartedEvent:
    def to_json(self) -> str:
        return json.dumps({"event": "EXECUTION_STARTED"})


@dataclass
class ExecutionAbortedEvent:
    reason: str

    def to_json(self) -> str:
        return json.dumps({"event": "EXECUTION_ABORTED", "reason": self.reason})


class ExecutionFinishedEvent:
    def to_json(self) -> str:
        return json.dumps({"event": "EXECUTION_FINISHED"})


Event = (
    ServerScriptConnectedEvent
    | ServerScriptDisconnectedEvent
    | EventQueueClosing
    | NewClientsConnectedEvent
    | ExecutionStartedEvent
    | ExecutionAbortedEvent
    | ExecutionFinishedEvent
)

# Messages for the ServerScript request queue


@dataclass
class IncomingRequestMessage:
    client_id: str
    data: dict


# Used for when a server script is overridden
class OverrideServerScriptMessage:
    pass


# Used for when a server script is interrupted via keyboard
class ShutdownServerScriptMessage:
    pass


RequestMessage = IncomingRequestMessage | OverrideServerScriptMessage
