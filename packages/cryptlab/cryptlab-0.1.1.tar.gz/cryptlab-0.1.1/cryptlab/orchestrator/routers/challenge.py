import asyncio
import secrets
from concurrent.futures import ThreadPoolExecutor
from loguru import logger
from fastapi import APIRouter, HTTPException, Request, Response
from pydantic import BaseModel

from cryptlab.client.pki import OrchestratedPKIConnection
import cryptlab.common.cfg as cfg
from cryptlab.client.orchestrated import ClientImporter, OrchestratedConnection
from cryptlab.common.exceptions import PKIEntryAlreadySet
from cryptlab.common.messages import (
    ExecutionAbortedEvent,
    ExecutionFinishedEvent,
    ExecutionStartedEvent,
    MessageQueue,
    NewClientsConnectedEvent,
    ServerDisconnected,
)
from cryptlab.orchestrator.clients.validator import (
    construct_action_schema,
    validate_action_list,
)
from cryptlab.orchestrator.dependencies import TokenDep
from cryptlab.orchestrator.serverscripts.bridge import Bridge

router = APIRouter(prefix="/api/v1")

@router.get("/healthcheck")
async def healthcheck():
    return {"result": "ok"}


@router.get("/token")
async def get_token(response: Response, token: TokenDep):
    response.set_cookie(key="token", value=token)
    return 200, response


class ExecConfig(BaseModel):
    n_clients: int
    actions: list[list]


class PKIDataEntry(BaseModel):
    value: str


@router.post("/pki/{key}")
async def upload_to_pki(
    request: Request, token: TokenDep, key: str, value: PKIDataEntry
):
    """Implement an append-only storage to be used as PKI

    This can be used by clients to upload e.g. their private keys
    and for other clients to retrieve them in an authentic manner.
    Entries are indexed by client_id and cannot be overwritten (so that players
    cannot do trivial substitution attacks).

    We need to ensure that players cannot place data before the honest client does.
    This is given by the unpredictability of (honest) client IDs.
    We bound the size of the PKI storage per token, so that (1) we do not get
    DoS'd, and (2) the player cannot just put data for all possible client IDs.

    We do, however, allow the player to just delete all entries in the PKI.
    """

    logger.info(
        "Got request for {} to put key={} and value={}", token, key, value.value
    )
    bridge: Bridge = request.app.state.bridge
    try:
        bridge.set_pki_entry(token, key, value.value)
    except PKIEntryAlreadySet:
        raise HTTPException(status_code=409, detail=f"{key} already set in PKI")


@router.get("/pki/{key}")
async def get_from_pki(request: Request, token: TokenDep, key: str):
    logger.info("Got request for {} to retrieve key={}", token, key)
    bridge: Bridge = request.app.state.bridge
    value = bridge.get_pki_entry(token, key)
    if value is not None:
        return {"result": value}
    else:
        raise HTTPException(status_code=404, detail=f"{key} not found in PKI")


@router.get("/actions")
async def get_actions():
    _, actions_enum = ClientImporter.get_client_class(cfg.CLIENT_PATH)
    schema = construct_action_schema(actions_enum)
    return {
        "max_clients": cfg.MAX_ORCHESTRATED_CLIENTS_PER_USER,
        "max_actions": cfg.MAX_ACTIONS,
        "actions_allowed": schema,
    }


@router.post("/exec")
async def run_client(request: Request, exec_config: ExecConfig, server_id: TokenDep):
    bridge: Bridge = request.app.state.bridge
    orch_to_serv = bridge.get_orch_to_serv_queue(server_id)

    if not orch_to_serv:
        raise HTTPException(status_code=400, detail="ServerScript not connected")

    n_clients = exec_config.n_clients
    actions = exec_config.actions

    client, actions_enum = ClientImporter.get_client_class(cfg.CLIENT_PATH)

    success, details = validate_action_list(n_clients, actions, actions_enum)

    if not success:
        raise HTTPException(
            status_code=400, detail=f"Malformed execution configuration: {details}"
        )

    logger.info("Exec config passed validation")

    loop = asyncio.get_running_loop()

    client_ids = []
    client_list = []
    client_queues = {}

    pki_conn = OrchestratedPKIConnection(bridge, server_id)

    for _ in range(n_clients):
        while True:
            # Generate unique random names
            client_id = secrets.token_hex(16)
            if client_id not in client_ids:
                break

        orch_to_client = MessageQueue()
        conn = OrchestratedConnection(
            client_id, server_id, orch_to_client, orch_to_serv, loop
        )
        cl = client(
            cfg.FLAG, conn, pki_connection=pki_conn, allowed_actions=actions_enum
        )
        client_list.append(cl)
        client_ids.append(client_id)
        client_queues[client_id] = orch_to_client

    bridge.register_clients(server_id, client_queues)
    await bridge.broadcast(server_id, NewClientsConnectedEvent(client_ids))

    logger.info("Clients created, starting execution")
    await bridge.broadcast(server_id, ExecutionStartedEvent())
    logger.info("Event broadcasted")

    for action in actions:
        client_number, *command = action
        cl = client_list[client_number]
        executor: ThreadPoolExecutor = request.app.state.executor
        future = executor.submit(cl.run_command, command)
        wrapped_future = asyncio.wrap_future(future)

        try:
            await asyncio.wait_for(wrapped_future, timeout=cfg.ACTION_TIMEOUT)
        except TimeoutError:
            logger.info(
                "Client-server interaction did not terminate in time. Aborting execution"
            )
            orch_to_serv = bridge.get_orch_to_serv_queue(server_id)
            assert orch_to_serv is not None
            await bridge.broadcast(server_id, ExecutionAbortedEvent("Client-server interaction did not terminate in time"))
            await bridge.send_message_to_all_clients(server_id, ServerDisconnected())
            raise HTTPException(
                status_code=400, detail=f"Client-server interaction did not terminate in time. Aborting execution"
            )

        if not wrapped_future.result():
            logger.info("Client ran into an error, aborting execution")
            await bridge.broadcast(server_id, ExecutionAbortedEvent("Client ran into an exception"))
            raise HTTPException(
                status_code=400, detail=f"Client ran into an error. Aborting execution"
            )
    else:
        await bridge.broadcast(server_id, ExecutionFinishedEvent())
