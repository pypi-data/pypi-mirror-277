from loguru import logger
from fastapi import APIRouter
from fastapi.responses import HTMLResponse

from cryptlab.common import cfg
from cryptlab.orchestrator.dependencies import TokenDep

router = APIRouter()


# @router.get("/")
# async def get_challenge_status2(token: TokenDep):
#     logger.info("Got token: {}", token)

#     # TODO: remove this
#     with open(cfg.PAGES_DIR + "/challenge.html") as f:
#         htmldata = f.read()

#     response = HTMLResponse(htmldata)
#     response.set_cookie(key="token", value=token)
#     return response
