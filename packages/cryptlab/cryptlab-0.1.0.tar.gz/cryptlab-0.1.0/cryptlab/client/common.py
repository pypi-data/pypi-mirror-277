from functools import wraps
from enum import Enum, EnumType, StrEnum
from typing import Any, Callable, ParamSpec, TypeVar
from loguru import logger

from cryptlab.client.pki import LocalPKIConnection
from cryptlab.common.exceptions import ServerClosedConnection

BaseClientChild = TypeVar("BaseClientChild", bound="BaseClient")

P = ParamSpec("P")

Handler = Callable[P, None]
WrappedHandler = Callable[P, bool]


class BaseActionEnum(StrEnum):
    pass


class BaseConnection:
    def get_client_id(self) -> str:
        raise NotImplementedError()

    def exec(self, command) -> dict[str, Any]:
        raise NotImplementedError()

    def close(self):
        raise NotImplementedError()


class LocalClientOrchestrator:
    def __init__(self, client_class: type): ...


class BaseClient:
    def __init__(
        self,
        server_connection: BaseConnection,
        allowed_actions: EnumType,
        pki_connection: LocalPKIConnection,
    ):
        self.conn = server_connection
        self.allowed_actions = allowed_actions
        self.pki_conn = pki_connection

    def get_client_id(self):
        return self.conn.get_client_id()

    def run_command(self, command: list | tuple | str | Enum) -> bool:
        match command:
            case [cmd, *args] | (cmd, *args):
                command = cmd
                arguments = args
            case cmd:
                command = cmd
                arguments = []

        if type(command) is str:
            command = command.lower()

        logger.info("Executing command {} with arguments {}", command, arguments)

        cmd_enum: Enum = self.allowed_actions(command)  # pyright: ignore
        handler = client_action.get_command_handler(cmd_enum)

        logger.info("Using command handler {}", handler.__name__)
        return handler(self, *arguments)

    def run_command_list(self, cmd_list: list):
        cmd_list = normalize_command_list(cmd_list)

        for cmd_entry in cmd_list:
            cmd, *args = cmd_entry

            # Here we disable type checking because, according to pyright an
            # Enum attribute ends up being an EnumType again instead of an Enum.
            cmd_enum: Enum = self.allowed_actions(cmd)  # pyright: ignore

            handler = client_action.get_command_handler(cmd_enum)

            success = handler(self, *args)

            if not success:
                logger.error(
                    "Command {} failed, terminating client execution.", cmd_entry
                )
                break

    def get_from_pki(self, key: str):
        return self.pki_conn.get(key)

    def push_to_pki(self, key: str, value: str):
        self.pki_conn.set(key, value)


def normalize_command_list(cmd_list: list) -> list[tuple[str, list]]:
    new_list = []

    for cmd_entry in cmd_list:
        match cmd_entry:
            case (cmd, *args):
                command = cmd
                arguments = args
            case cmd:
                command = cmd
                arguments = []

        if type(arguments) != list:
            arguments = [arguments]

        new_list.append((command, *arguments))

    return new_list


# pylint: disable=invalid-name
class client_action:
    """A decorator class to register an action that the client can be asked to execute"""

    _handlers: dict[Enum, WrappedHandler] = {}

    def __init__(self, command: Enum):
        self.command = command

    def wrap_handler(self, handler: Handler) -> WrappedHandler:
        # Wrap the handler to handle the server closing and any unexpected exceptions
        @wraps(handler)
        def _handler_inner(*args, **kwargs):
            try:
                handler(*args, **kwargs)
                return True
            except ServerClosedConnection:
                logger.info("Server closed the connection! Exiting")
            except Exception as e:
                logger.info(
                    "Unexpected error ({}: {}). Exiting...", type(e).__name__, e
                )
            return False

        return _handler_inner

    def __call__(self, handler: Handler) -> Handler:
        self._handlers[self.command] = self.wrap_handler(handler)
        return handler

    @classmethod
    def get_command_handler(cls, command: Enum) -> WrappedHandler:
        """Returns the handler for the specified command

        Raises KeyError if the command has no registered handler
        """

        return cls._handlers[command]

    @classmethod
    def list_commands(cls) -> list[str]:
        """Returns the list of all registered commands"""

        return list(key.name for key in cls._handlers.keys())
