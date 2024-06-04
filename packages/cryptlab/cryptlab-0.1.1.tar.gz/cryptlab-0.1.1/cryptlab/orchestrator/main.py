import asyncio
import signal
import uvicorn
from functools import partial
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
from concurrent.futures import ThreadPoolExecutor

import cryptlab.common.cfg as cfg
from cryptlab.orchestrator.logger import init_logging
from cryptlab.orchestrator.routers import healthcheck, challenge, root, websocket
from cryptlab.orchestrator.serverscripts.bridge import Bridge
from cryptlab.orchestrator.serverscripts.tcphandler import TCPOrchestrator

# Override FastAPI logging to integrate with Loguru (as much as we can)
init_logging()


# This is a bit of a hack, but FastAPI does not allow us to kill endless loops cleanly
# Setting a shutdown handler (e.g. inside the lifespan method) won't work, since it
# is called only after all background tasks have terminated, which will never happen
# since we have some endless loops...
def stop_server(bridge: Bridge, prev_handler, *args):
    logger.info("Stopping all conns")
    asyncio.create_task(bridge.close())
    logger.info("Stopped all conns")

    prev_handler(*args)


@asynccontextmanager
async def lifespan(app: FastAPI):
    bridge = Bridge()
    app.state.bridge = bridge
    app.state.executor = ThreadPoolExecutor(cfg.MAX_ORCHESTRATED_CLIENT_WORKERS)

    orchestrator = TCPOrchestrator(bridge)

    for sig in (signal.SIGINT, signal.SIGTERM):
        # Set the signal to stop all websockets and TCP conns
        _prev_handler = signal.getsignal(sig)
        signal.signal(sig, partial(stop_server, bridge, _prev_handler))

    # Start the TCP Orchestrator
    task = asyncio.create_task(
        asyncio.start_server(
            orchestrator.handle, cfg.TCP_ORCHESTRATOR_HOST, cfg.TCP_ORCHESTRATOR_PORT
        )
    )

    # Yield control back to the app
    yield

    task.cancel()


# Initialize FastAPI for the browser interface
app = FastAPI(lifespan=lifespan)
# app.include_router(healthcheck.router)
app.include_router(challenge.router)
# app.include_router(root.router)
app.include_router(websocket.router)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://0.0.0.0", "http://localhost", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def run_orchestrator():
    try:
        uvicorn.run(
            app, host=cfg.ORCHESTRATOR_WEBAPP_HOST, port=cfg.ORCHESTRATOR_WEBAPP_PORT
        )
    except KeyboardInterrupt:
        logger.info("Shutting down Orchestrator...")

if __name__ == "__main__":
    run_orchestrator()
