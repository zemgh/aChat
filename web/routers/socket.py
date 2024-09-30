from fastapi import APIRouter
from starlette.websockets import WebSocket, WebSocketDisconnect

from dependencies.ws import WebSocketConnectionsManager, WebSocketConsumer

router = APIRouter(prefix='/ws', tags=['websocket'])

manager = WebSocketConnectionsManager()


@router.websocket('/{user_id}')
async def websocket_endpoint(websocket: WebSocket, user_id: int):
    consumer = WebSocketConsumer(manager, websocket, user_id)
    await manager.add(consumer)
    await consumer.run()



