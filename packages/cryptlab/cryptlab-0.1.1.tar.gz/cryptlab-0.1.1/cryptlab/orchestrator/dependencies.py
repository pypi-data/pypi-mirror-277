import secrets
from typing import Annotated, Union

from fastapi import Cookie, Depends, Request, WebSocket

NullableTokenDep = Annotated[Union[str, None], Cookie()]


def token_dep(request: Request, token: NullableTokenDep = None):
    if token is None:
        token = secrets.token_hex(32)
    # We register the token regardless
    request.app.state.bridge.register_token(token)
    return token


TokenDep = Annotated[str, Depends(token_dep)]


def ws_token_dep(websocket: WebSocket, token: NullableTokenDep = None):
    if token is None:
        token = secrets.token_hex(32)
    # We register the token regardless
    websocket.app.state.bridge.register_token(token)
    return token


WSTokenDep = Annotated[str, Depends(ws_token_dep)]
