from fastapi import APIRouter

router = APIRouter(prefix='/api/v1/topics', tags=['topics'])


@router.post('/create')
async def create_topic():
    return {'message': 'create topic'}


@router.get('/{id}')
async def get_topic():
    return {'message': 'get topic'}


@router.put('/{id}/update')
async def update_topic():
    return {'message': 'update topic'}


@router.delete('/{id}/delete')
async def delete_topic():
    return {'message': 'delete topic'}