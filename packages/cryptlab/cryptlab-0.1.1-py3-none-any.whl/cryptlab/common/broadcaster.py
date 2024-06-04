from fastapi import WebSocketDisconnect
from cryptlab.common.messages import Event


class AsyncEventListener:
    async def send_message(self, message: Event):
        raise NotImplementedError()

    async def close(self):
        raise NotImplementedError()


class AsyncEventBroadcaster:
    def __init__(self):
        self.listeners: set[AsyncEventListener] = set()

    def add_listener(self, listener: AsyncEventListener):
        self.listeners.add(listener)

    async def remove_listener(self, listener: AsyncEventListener):
        self.listeners.remove(listener)
        await listener.close()

    async def broadcast(self, message: Event):
        # Since we're iterating over listeners, we can't remove while iterating
        # so we simply store all listeners that should be removed
        to_remove = []

        for listener in self.listeners:
            try:
                await listener.send_message(message)
            except WebSocketDisconnect:
                to_remove.append(listener)

        for listener in to_remove:
            await self.remove_listener(listener)
