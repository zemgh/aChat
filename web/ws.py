import asyncio
import json
from typing import Dict
from starlette.websockets import WebSocket, WebSocketDisconnect


class WebSocketConnectionsManager:
    def __init__(self):
        self._connections: Dict[int, 'ChatConsumer'] = {}


    async def add(self, consumer: 'ChatConsumer'):
        if consumer.user_id not in self._connections:
            connection: Dict[int, WebSocket] = consumer.get_dict()
            self._connections.update(connection)
        else:
            await consumer.close()


    async def remove(self, user_id: int):
        self._connections.pop(user_id, None)


class BaseConsumer:
    ALLOWED_MESSAGE_TYPES = []


    def __init__(self, manager: 'WebSocketConnectionsManager', websocket: 'WebSocket', user_id: int):
        self._manager = manager
        self._websocket = websocket
        self._user_id = user_id


    async def run(self):
        await self._websocket.accept()
        await self._websocket.send_json({'type': 'chat_message', 'message': 'Hello World!'})

        try:
            while True:
                data = await self._websocket.receive_json()
                await self._handle_message(data)

        except WebSocketDisconnect:
            await self._manager.remove(self._user_id)


    async def _handle_message(self, data: dict):
        message_type = data.get('type')
        if message_type and message_type in self.ALLOWED_MESSAGE_TYPES:
            method = getattr(self, '_' + message_type)
            await method(data)

    async def _send(self, data):
        await self._websocket.send_json(data)


    async def close(self):
        await self._websocket.close()


    def get_dict(self):
        return {self._user_id: self}


    @property
    def user_id(self):
        return self._user_id


class ChatConsumer(BaseConsumer):
    ALLOWED_MESSAGE_TYPES = ['chat_message', 'find_chat', 'cancel_search', 'close_chat']
    active_chat: int = None
    search_chat: bool = False

    async def start_chat(self, data: dict):
        if self.search_chat:
            self.search_chat = False
            self.active_chat = data['chat_id']
            send_data = {'type': 'new_chat'}
            await self._send(send_data)
            print('method start_chat')

    async def _chat_message(self, data: dict):
        if self.active_chat:
            await self._send(data)
            print('method _chat_message')


    async def _find_chat(self, data: dict):
        self.search_chat = True
        send_data = {'type': 'find_chat'}
        await self._send(send_data)
        print('method _find_chat')

        asyncio.create_task(self.test())

    async def test(self):
        await asyncio.sleep(3)
        await self.start_chat({'chat_id': 1})

    async def _cancel_search(self, data: dict):
        self.search_chat = False
        await self._send({'type': 'cancel_search'})
        print('method _cancel_search')


    async def _close_chat(self, data: dict):
        self.active_chat = None
        await self._send({'type': 'close_chat'})
        print('method _close_chat')

