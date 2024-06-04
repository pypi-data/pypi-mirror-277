import asyncio
from fastapi import WebSocket
from cryptlab.common.broadcaster import AsyncEventListener
from cryptlab.common.messages import Event, EventQueueClosing


class WSListener(AsyncEventListener):
    def __init__(self, websocket: WebSocket, event: asyncio.Event):
        self.websocket = websocket
        self.event = event

    async def send_message(self, message: Event):
        match message:
            case EventQueueClosing():
                await self.close()
                return
            case _:
                await self.websocket.send_text(message.to_json())

    async def close(self):
        try:
            await self.websocket.close(code=1001)
        except RuntimeError:
            # Sometimes closing the websocket won't work, but we don't care
            pass
        self.event.set()
