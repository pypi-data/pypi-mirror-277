import asyncio
from cryptlab.common.messages import ServerScriptConnectedEvent
from loguru import logger
from fastapi import APIRouter, WebSocket

from cryptlab.orchestrator.dependencies import WSTokenDep
from cryptlab.orchestrator.serverscripts.bridge import Bridge
from cryptlab.orchestrator.clients.wslistener import WSListener

router = APIRouter()

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket, token: WSTokenDep):
    await websocket.accept()
    logger.info("Started ws for token {}", token)
    bridge: Bridge = websocket.app.state.bridge
    event = asyncio.Event()
    bridge.register_listener(token, WSListener(websocket, event))

    if name := bridge.is_server_script_connected(token):
        await bridge.broadcast(token, ServerScriptConnectedEvent(name))

    await event.wait()
