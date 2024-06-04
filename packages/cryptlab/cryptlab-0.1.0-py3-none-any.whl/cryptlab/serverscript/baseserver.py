from functools import partial
import socket
import threading
import socketserver
import json
from queue import Queue
from typing import Any, Callable, TypeVar

from loguru import logger

from cryptlab.common.exceptions import InvalidMessageError
from cryptlab.common.messages import (
    OverrideServerScriptMessage,
    IncomingRequestMessage,
    RequestMessage,
    ShutdownServerScriptMessage,
)

RequestQueue = Queue[RequestMessage]

# A type variable for any instance of a class that inherits from CommandServer
BaseServerChild = TypeVar("BaseServerChild", bound="BaseServer")

# A init handler takes self, and returns nothing
InitHandler = Callable[[BaseServerChild], None]

# A command handler takes self, a clientID, an unmarshalled JSON, and returns nothing
Handler = Callable[[BaseServerChild, str, dict[str, Any]], None]

# A message is a dict that can be converted to JSON
# Note that JSON specifies that keys *must* be strings and will force
# them to be string if necessary.
Message = dict[str, Any]

ResponseCallback = Callable[[Message], None]


class ResponseRouter:
    def __init__(self):
        self.lock = threading.Lock()
        self.routes: dict[str, ResponseCallback] = {}

    def register_response_route(self, client_id: str, conn: ResponseCallback):
        with self.lock:
            if not client_id.startswith("remote.") and not client_id.startswith(
                "local."
            ):
                raise ValueError(f"Cannot accept untagged client_id {client_id}")

            self.routes[client_id] = conn

    def send_response(self, aug_client_id: str, response: Message):
        with self.lock:
            self.routes[aug_client_id](response)


# TODO: Maybe a bit awkward as an interface right now, might make a new method for adding request queues
class BaseConnectionListener:
    def start(self):
        raise NotImplementedError()

    def close(self):
        raise NotImplementedError()


class TCPConnectionListener(BaseConnectionListener):
    """TCP Connection that listens for incoming packets from the Orchestrator"""

    def __init__(
        self,
        host: str,
        port: int,
        request_queue: RequestQueue,
        response_router: ResponseRouter,
        *args,
        **kwargs,
    ) -> None:
        self.fd = socket.create_connection((host, port)).makefile("rw")
        self.authenticated = False
        self.request_queue = request_queue
        self.response_router = response_router
        self.exit = threading.Event()
        self.clients_seen: set[str] = set()
        super().__init__(*args, **kwargs)

    def authenticate(self, token: str):
        if self.authenticated:
            raise Exception("Already authenticated")

        # Authenticate the listener
        self.fd.write(json.dumps({"auth_code": token}) + "\n")
        self.fd.flush()

        res = json.loads(self.fd.readline())
        if "error" in res:
            raise Exception(f"Could not connect. Error: {res['error']}")

        script_name = res["success"]
        return script_name

    def _send_response_callback(self, client_id: str, response: Message):
        self.fd.write(json.dumps({"client_id": client_id, "data": response}) + "\n")
        self.fd.flush()

    def _listen_for_commands(self):
        while True:
            if self.exit.is_set():
                break

            try:
                line = self.fd.readline()

                if not line:
                    self.request_queue.put(OverrideServerScriptMessage())
                    break

                res = json.loads(line)

                if "client_id" not in res:
                    raise InvalidMessageError("Missing client_id in message")

                client_id = res["client_id"]

                # Within the serverscript, we only work with augmented_client_ids
                # This separates the IDs of orchestrated and local clients and allows us to always
                # know where to route messages
                augmented_client_id = "remote." + client_id

                if augmented_client_id not in self.clients_seen:
                    self.response_router.register_response_route(
                        augmented_client_id,
                        partial(self._send_response_callback, client_id),
                    )
                    self.clients_seen.add(augmented_client_id)

                if "data" not in res:
                    raise InvalidMessageError("Missing data in message")
                data = res["data"]

                request = IncomingRequestMessage(augmented_client_id, data)
                self.request_queue.put(request)
            except Exception as e:
                logger.error("Encountered unparseable message. Skipping. {}", e)
                continue
        logger.info("Exiting TCPConnectionListener")

    def start(self):
        self.t = threading.Thread(target=self._listen_for_commands, daemon=True)
        self.t.start()

    def close(self):
        self.exit.set()


class LocalClientListener(socketserver.StreamRequestHandler):
    """TCP Server for local clients to connect to"""

    def __init__(
        self,
        request_queue: RequestQueue,
        response_router: ResponseRouter,
        exit: threading.Event,
        *args,
        **kwargs,
    ):
        self.exit = exit
        self.request_queue = request_queue
        self.response_router = response_router
        self.running = True

        super().__init__(*args, **kwargs)

    def send_message(self, obj: Message):
        """Send a JSON-formatted response to the client.

        Args:
            obj (dict): the response object
        """
        res = json.dumps(obj) + "\n"

        try:
            self.wfile.write(res.encode())
            self.wfile.flush()
        except (BrokenPipeError, ConnectionResetError):
            # Client has disconnected, close connection silently
            self.close_connection()

    def read_message(self) -> Message:
        """Parse a JSON-formatted message from the client.

        Returns:
            dict: a dictionary representing the input JSON message.
        """
        msg = self.rfile.readline()
        return json.loads(msg)

    def close_connection(self) -> None:
        """Close the connection by exiting the `handle` method"""

        self.running = False

    def handle(self) -> None:
        try:
            msg = self.read_message()
        except json.decoder.JSONDecodeError:
            self.send_message({"res": "Failed to execute command: malformed JSON"})
            return
        except ConnectionResetError:
            logger.info("Connection reset by client")
            return

        if "client_id" not in msg:
            self.send_message({"error": "Missing client_id in first message"})
            return

        client_id = msg["client_id"]
        self.client_id = "local." + client_id

        self.response_router.register_response_route(self.client_id, self.send_message)
        self.send_message({"res": "Success"})

        while self.running and not self.exit.is_set():
            try:
                msg = self.read_message()
            except json.decoder.JSONDecodeError:
                self.send_message({"res": "Failed to execute command: malformed JSON"})
                continue
            except ConnectionResetError:
                break

            self.request_queue.put(IncomingRequestMessage(self.client_id, msg))

    def finish(self) -> None:
        """Clean up after the client disconnects. Automatically called by TCPServer"""
        self.wfile.close()

    @classmethod
    def start_server(cls, host: str, port: int, ipv6: bool = False, **kwargs) -> None:
        """Start the TCP server on the given port

        Args:
            host (str): the host on which to listen
            port (int): the TCP port on which to listen
            kwargs: all the additional parameters that will be injected
                    into the request handler
        """

        def _wrapped():
            # Inject our values by partial application to the class
            cls_injected = lambda request, client_address, server: cls(
                **kwargs, request=request, client_address=client_address, server=server
            )

            class TCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
                """A TCP Server that allows for multiple simultaneous connections and port reuse"""

                address_family = socket.AF_INET6 if ipv6 else socket.AF_INET
                allow_reuse_address = True

            with TCPServer((host, port), cls_injected) as server:
                server.serve_forever()

        t = threading.Thread(target=_wrapped, daemon=True)
        t.start()


class BaseServer:
    """Base class for ServerScripts

    This class exposes a TCP server for local clients and connects to the Orchestrator for
    interaction with the remote clients. In order to make interleaving not an issue, we serialize
    all the interactions with clients by enqueueing everything in a single requests queue.
    Each request is then handled individually. This is clearly not good for server performance, but in this
    case, it's not an issue.
    """

    def __init__(
        self,
        request_queue: RequestQueue,
        response_router: ResponseRouter,
        tcp_listener: BaseConnectionListener,
        local_client_listener_exit: threading.Event,
        *args,
        **kwargs,
    ) -> None:
        self.running = True
        self.request_queue = request_queue
        self.response_router = response_router
        self.has_send_message_been_called = False
        self.tcp_listener = tcp_listener
        self.local_client_listener_exit = local_client_listener_exit
        super().__init__(*args, **kwargs)

    @classmethod
    def start_server(
        cls,
        orch_host: str,
        orch_port: int,
        local_listener_host: str,
        local_listener_port: int,
        token: str,
    ):
        response_router = ResponseRouter()
        request_queue = Queue()

        try:
            tcp_listener = TCPConnectionListener(
                orch_host, orch_port, request_queue, response_router
            )
            script_name = tcp_listener.authenticate(token)
            tcp_listener.start()
            logger.info("Connected to orchestrator, we are {}", script_name)

            local_client_listener_exit = threading.Event()

            LocalClientListener.start_server(
                host=local_listener_host,
                port=local_listener_port,
                request_queue=request_queue,
                response_router=response_router,
                exit=local_client_listener_exit,
            )

            cls(
                request_queue, response_router, tcp_listener, local_client_listener_exit
            ).start().join()
        except KeyboardInterrupt:
            request_queue.put(ShutdownServerScriptMessage())
        logger.info("Server shut down succesfully")

    def _send_message_unchecked(self, client_id: str, message: Message):
        self.response_router.send_response(client_id, message)

    def send_message(self, client_id: str, message: Message):
        if self.has_send_message_been_called:
            raise RuntimeError("You run send_message only once for each request")

        self.response_router.send_response(client_id, message)
        self.has_send_message_been_called = True

    def start(self):
        t = threading.Thread(target=self._run)
        t.start()
        return t

    def _run(self):
        try:
            while True:
                request = self.request_queue.get()

                match request:
                    case OverrideServerScriptMessage():
                        logger.info(
                            "Another ServerScript has been activated with the same token. Shutting down..."
                        )
                        break
                    case ShutdownServerScriptMessage():
                        logger.info("ServerScript shutting down by user request")
                        break
                    case IncomingRequestMessage(client_id, data):
                        with logger.contextualize(client=client_id):
                            if "command" not in data:
                                logger.error(
                                    "Client sent request without the `command` field"
                                )
                                self.send_message(
                                    client_id,
                                    {
                                        "error": "Failed to execute command: `command` field missing"
                                    },
                                )
                                continue

                            try:
                                handler = on_command.get_command_handler(
                                    data["command"]
                                )
                            except KeyError:
                                logger.error(
                                    "Client sent request with invalid `command` name"
                                )
                                self.send_message(
                                    client_id,
                                    {
                                        "error": "Failed to execute command: `command` name not valid"
                                    },
                                )
                                continue

                            # The serverscript will crash if errors are not caught, but this is ok
                            # It's the responsibility of the player to make a server that does not crash
                            self.has_send_message_been_called = False
                            handler(self, client_id, data)
                            if not self.has_send_message_been_called:
                                raise RuntimeError(
                                    f"You must run send_message exactly once for each request (missing call on {data['command']})"
                                )
                    case _:
                        raise InvalidMessageError()
        except Exception as e:
            logger.error("Server encountered an error, shutting down...")
            logger.error("Exception info: {} - {}", type(e).__name__, e)
        finally:
            self.tcp_listener.close()
            self.local_client_listener_exit.set()


class on_command:
    """A decorator class used to register a handler to be called on a specified command"""

    _handlers: dict[str, Handler] = {}

    def __init__(self, command: str):
        self.command = command

    def __call__(self, handler: Handler) -> Handler:
        self._handlers[self.command] = handler
        return handler

    @classmethod
    def get_command_handler(cls, command: str) -> Handler:
        """Returns the handler for the specified command

        Raises KeyError if the command has no registered handler
        """

        return cls._handlers[command]

    @classmethod
    def list_commands(cls) -> list[str]:
        """Returns the list of all registered commands"""

        return list(cls._handlers.keys())


class on_startup:
    """A decorator class used to register a handler to be called at startup"""

    _handler: InitHandler | None = None

    def __call__(self, handler: InitHandler) -> InitHandler:
        self.__class__._handler = handler
        return handler

    @classmethod
    def run_startup_handler(cls, obj: BaseServer):
        """Executes the handler registered for startup, if present"""

        if cls._handler is not None:
            cls._handler(obj)
