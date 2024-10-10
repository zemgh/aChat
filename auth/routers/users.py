from fastapi import APIRouter

router = APIRouter(prefix='/api/v1/users', tags=['users'])


@router.post('/create')
async def create_user():
    return {'message': 'create user'}


@router.get('/{id}')
async def get_user():
    return {'message': 'get user'}


@router.put('/{id}/update')
async def update_user():
    return {'message': 'update user'}


@router.delete('/{id}/delete')
async def delete_user():
    return {'message': 'delete user'}