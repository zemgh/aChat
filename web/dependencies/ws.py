from typing import Dict
from starlette.websockets import WebSocket, WebSocketDisconnect


class WebSocketConnectionsManager:
    def __init__(self):
        self._connections: Dict[int, 'WebSocketConsumer'] = {}

    async def add(self, consumer: 'WebSocketConsumer'):
        if consumer.user_id not in self._connections:
            connection: Dict[int, WebSocket] = consumer.get_dict()
            self._connections.update(connection)
        else:
            await consumer.close()

    async def remove(self, user_id: int):
        self._connections.pop(user_id, None)


class WebSocketConsumer:
    def __init__(self, manager: 'WebSocketConnectionsManager', websocket: 'WebSocket', user_id: int):
        self._manager = manager
        self._websocket = websocket
        self._user_id = user_id

    async def run(self):
        await self._websocket.accept()
        await self._websocket.send_json({'message': 'Hello World!'})

        try:
            while True:
                data = await self._websocket.receive_text()
                await self._websocket.send_text(data)

        except WebSocketDisconnect:
            await self._manager.remove(self._user_id)

    async def close(self):
        await self._websocket.close()

    def get_dict(self):
        return {self._user_id: self}

    @property
    def user_id(self):
        return self._user_id
