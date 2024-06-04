from enum import EnumType
import sys

from cryptlab.client.pki import LocalPKIConnection
from loguru import logger

from cryptlab.client.common import BaseClient
from cryptlab.client.local import TCPConnection


def orchestrate_clients(
    flag: str,
    token: str,
    configuration: dict,
    client_class: type,
    allowed_actions: EnumType,
    host: str,
    port: int,
    pki_host: str,
):
    n_clients = configuration["n_clients"]
    actions = configuration["actions"]
    clients: list[BaseClient] = []
    pki_conn = LocalPKIConnection(pki_host, token)
    for _ in range(n_clients):
        conn = TCPConnection(host, port)
        cl = client_class(flag, conn, allowed_actions=allowed_actions, pki_connection=pki_conn)
        clients.append(cl)

    logger.info("Created {} local clients", n_clients)
    for i, cl in enumerate(clients):
        logger.info(f"Client {i}: {cl.get_client_id()}")

    for action in actions:
        client_idx, *command = action
        with logger.contextualize(client_id=clients[client_idx].get_client_id()):
            res = clients[client_idx].run_command(command)
            if not res:
                break


def setup_logging():
    logger.remove(0)
    fmt = "<green>{time:HH:mm:ss:SSS}</green> | <level>{level: <6}</level> | <green>[{extra[client_id]}]</green> - <level>{message}</level>"
    logger.add(sys.stderr, format=fmt)
    logger.configure(extra={"client_id": "LOCAL"})
