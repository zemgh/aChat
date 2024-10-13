from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from db import get_db
from models import User
from repository import UserRepository
from schemas.users import UserCreateSchema

router = APIRouter(prefix='/api/v1/users', tags=['users'])


@router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_user(db: Annotated[AsyncSession, Depends(get_db)], data: UserCreateSchema):
    repository = UserRepository(db)
    created_user = await repository.create_user(data)
    return created_user


@router.get('/{user_id}', status_code=status.HTTP_200_OK)
async def get_user(db: Annotated[AsyncSession, Depends(get_db)], user_id: int):
    repository = UserRepository(db)
    user = await repository.get_user(user_id)
    return user


@router.put('/{id}/update')
async def update_user():
    return {'message': 'update user'}


@router.delete('/{id}/delete')
async def delete_user():
    return {'message': 'delete user'}