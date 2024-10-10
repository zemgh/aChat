from fastapi import APIRouter

router = APIRouter(prefix='/api/v1/genders', tags=['genders'])


@router.post('/create')
async def create_gender():
    return {'message': 'create gender'}


@router.get('/{id}')
async def get_gender():
    return {'message': 'get gender'}


@router.put('/{id}/update')
async def update_gender():
    return {'message': 'update gender'}


@router.delete('/{id}/delete')
async def delete_gender():
    return {'message': 'delete gender'}