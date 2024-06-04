from enum import EnumType
import sys

from loguru import logger

from cryptlab.client.common import BaseClient
from cryptlab.client.local import TCPConnection


def orchestrate_clients(
    flag: str,
    client_class: type,
    n_clients: int,
    host: str,
    port: int,
    actions: list[tuple],
    allowed_actions: EnumType,
):
    clients: list[BaseClient] = []
    for _ in range(n_clients):
        conn = TCPConnection(host, port)
        cl = client_class(flag, conn, allowed_actions=allowed_actions)
        clients.append(cl)

    logger.info("Created {} local clients")
    for i, cl in enumerate(clients):
        logger.info(f"Client {i}: {cl.get_client_id()}")

    for action in actions:
        client_idx, *command = action
        with logger.contextualize(client_id=clients[client_idx].get_client_id()):
            clients[client_idx].run_command(command)


def setup_logging():
    logger.remove(0)
    fmt = "<green>{time:HH:mm:ss:SSS}</green> | <level>{level: <6}</level> | <green>[{extra[client_id]}]</green> - <level>{message}</level>"
    logger.add(sys.stderr, format=fmt)
    logger.configure(extra={"client_id": "LOCAL"})
