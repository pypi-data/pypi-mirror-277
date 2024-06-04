import asyncio
from enum import EnumType
import sys
import importlib
import importlib.util
import inspect
from pathlib import Path
from typing import Any

from loguru import logger

import cryptlab.common.cfg as cfg
from cryptlab.common.exceptions import InvalidMessageError, ServerClosedConnection
from cryptlab.client.common import BaseActionEnum, BaseClient, BaseConnection
from cryptlab.common.messages import (
    ClientDisconnected,
    DataMessage,
    Message,
    MessageQueue,
    ServerDisconnected,
)

""" Boilerplate for clients, orchestrated version

Rather than communicating through TCP, the clients here are run by spinning up
a new client instance within the orchestrator and equipping them with two queues
which they can use to (bi-directionally) communicate with the server.

Because clients may be long-running, we want them to "sort-of" be async.
Concretely, we run each client in a different thread (more specifically, we use
a ThreadPoolExecutor) while still using asyncio queues, as the orchestrator
has to read them in async. We will need then to encapsulate the client side of
queues in a thread-safe manner, using Futures and `call_soon_threadsafe`.
"""


class OrchestratedConnection(BaseConnection):
    def __init__(
        self,
        client_id: str,
        server_script_id: str,
        orch_to_client: MessageQueue,
        client_to_orch: MessageQueue,
        loop: asyncio.AbstractEventLoop,
        *args,
        **kwargs,
    ):
        self.client_id = client_id
        self.server_script_id = server_script_id
        self.orch_to_client = orch_to_client
        self.client_to_orch = client_to_orch
        self.loop = loop
        super().__init__(*args, **kwargs)

    def get_client_id(self) -> str:
        return self.client_id

    def exec(self, command) -> dict[str, Any]:
        # Send the command to the serverscript
        message = DataMessage(self.client_id, self.server_script_id, command)
        asyncio.run_coroutine_threadsafe(
            self.client_to_orch.put(message), self.loop
        ).result()

        # We expect a response from the serverscript
        future = asyncio.run_coroutine_threadsafe(self.orch_to_client.get(), self.loop)

        try:
            response: Message = future.result(
                timeout=cfg.SERVER_SCRIPT_RESPONSE_TIMEOUT
            )
        except TimeoutError as e:
            logger.warning(
                "Serverscript did not reply in {} seconds, aborting execution.",
                cfg.SERVER_SCRIPT_RESPONSE_TIMEOUT,
            )
            raise e

        match response:
            case ServerDisconnected():
                raise ServerClosedConnection()
            case DataMessage(client_id, server_script_id, data):

                if client_id != self.client_id:
                    raise InvalidMessageError(
                        f"Received a message meant for client {client_id}, but we are {self.client_id}"
                    )

                if server_script_id != self.server_script_id:
                    raise InvalidMessageError(
                        f"Received a message from {server_script_id}, but we are {self.server_script_id}"
                    )

                return data
            case _:
                raise InvalidMessageError("Invalid message type received")

    def close(self):
        self.loop.call_soon_threadsafe(self.client_to_orch.put, ClientDisconnected())


def get_strict_subclass_in_module(base_class: type, module) -> type:
    """Given a module, finds the class that subclasses base_class

    Raises a ValueError if no such class or more than one class is found.
    """
    candidates = []

    for _, obj in inspect.getmembers(module):
        if (
            inspect.isclass(obj)
            and obj is not base_class
            and issubclass(obj, base_class)
        ):
            candidates.append(obj)

    if len(candidates) == 0:
        raise ValueError("No client found. Please subclass BaseClient.")

    if len(candidates) > 1:
        raise ValueError(
            "Too many clients found. Please subclass BaseClient only once per file."
        )

    return candidates[0]


class ClientImporter:
    _cache: dict = {}

    @classmethod
    def get_client_class(cls, path: str) -> tuple[type, EnumType]:
        """Given a path, dynamically imports a client and returns it

        Opens the file at `path` and tries to import the first class that subclasses BaseClient.
        An object is initialized by the class with the correct OrchestratedConnection and the flag.
        Classes are cached in order to save time. Note that this means that a module is loaded only
        once and modifications will not propagate until the entire orchestrator is restarted.
        """

        # Make path absolute, normalize and obtain the module name
        # WARNING: importing a file will execute all the global statements in the file.
        # Only import trusted files.

        path_obj = Path(path).resolve()

        if path_obj in cls._cache:
            client, actions = cls._cache[path_obj]
        else:
            module_name = path_obj.name.removesuffix(".py")

            spec = importlib.util.spec_from_file_location(module_name, path_obj)

            if spec is None or spec.loader is None:
                raise ValueError("Invalid path or module name for client script")

            module = importlib.util.module_from_spec(spec)

            if module is None:
                raise ValueError("Failed to extract module from import specification")

            sys.modules[module_name] = module
            spec.loader.exec_module(module)

            client_module = importlib.import_module(module_name)

            actions = get_strict_subclass_in_module(BaseActionEnum, client_module)
            client = get_strict_subclass_in_module(BaseClient, client_module)

            cls._cache[path_obj] = (client, actions)

        return client, actions
