from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from starlette import status


SQLALCHEMY_DATABASE_URL = 'postgresql+asyncpg://aChat_auth_user:qwerty@localhost:5432/aChat_auth_db'

engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)
async_session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
Base = declarative_base()


async def get_db() -> AsyncSession:
    try:
        async with async_session() as session:
            yield session
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={'message': 'Database Error'}
        )