from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from db import get_db
from repository import GenderRepository
from schemas.genders import GenderCreateSchema

router = APIRouter(prefix='/api/v1/genders', tags=['genders'])


@router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_gender(db: Annotated[AsyncSession, Depends(get_db)], data: GenderCreateSchema):
    repository = GenderRepository(db)
    gender = await repository.create_gender(data)
    return gender


@router.get('/{gender_id}', status_code=status.HTTP_200_OK)
async def get_gender(db: Annotated[AsyncSession, Depends(get_db)], gender_id: int):
    repository = GenderRepository(db)
    user = await repository.get_gender(gender_id)
    return user


@router.put('/{id}/update')
async def update_gender():
    return {'message': 'update gender'}


@router.delete('/{id}/delete')
async def delete_gender():
    return {'message': 'delete gender'}