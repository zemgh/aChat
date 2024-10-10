from fastapi import APIRouter
from starlette.websockets import WebSocket

from ws import WebSocketConnectionsManager, ChatConsumer

router = APIRouter(prefix='/ws', tags=['websocket'])

manager = WebSocketConnectionsManager()


@router.websocket('/{user_id}')
async def websocket_endpoint(websocket: WebSocket, user_id: int):
    consumer = ChatConsumer(manager, websocket, user_id)
    await manager.add(consumer)
    await consumer.run()



