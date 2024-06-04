import secrets
import socket
import json
from typing import Any


from cryptlab.client.common import BaseConnection

""" Boilerplate for clients, locally-run version """


class TCPConnection(BaseConnection):
    def __init__(self, host: str, port: int, *args, **kwargs):
        self.fd = socket.create_connection((host, port)).makefile("rw")
        self.client_id = secrets.token_hex(16)
        auth_msg = {"client_id": self.client_id}
        self.fd.write(json.dumps(auth_msg) + "\n")
        self.fd.flush()

        msg = json.loads(self.fd.readline())
        if "error" in msg:
            Exception(f"Error during client auth: {msg['error']}")

        super().__init__(*args, **kwargs)

    def get_client_id(self) -> str:
        return self.client_id

    def exec(self, command: dict[str, Any]) -> dict[str, Any]:
        """Serialize `command` to JSON and send to the server, then deserialize the response"""

        self.fd.write(json.dumps(command) + "\n")
        self.fd.flush()
        line = self.fd.readline()
        return json.loads(line)

    def close(self) -> None:
        self.fd.close()
