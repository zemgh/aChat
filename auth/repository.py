import bcrypt
from fastapi import HTTPException
from sqlalchemy import insert, select
from sqlalchemy.exc import IntegrityError
from starlette import status

from models import User, Gender
from schemas.genders import GenderResponseSchema
from schemas.users import UserResponseSchema


class BaseRepository:
    response_schema = None

    @staticmethod
    def _row_to_model(result):
        row = result.fetchone()
        model = row[0]
        return model

    def _get_response_schema(self, row=None, model=None):
        if row:
            model = self._row_to_model(row)
        data = model.to_response_dict()
        return self.response_schema(**data)


class UserRepository(BaseRepository):
    response_schema = UserResponseSchema

    def __init__(self, db):
        self._db = db

    async def create_user(self, data):
        try:
            query_data = data.dict()
            query_data['password'] = self._hash_password(data.password.get_secret_value())

            query = insert(User).values(**query_data).returning(User)
            row = await self._db.execute(query)
            await self._db.commit()

            return self._get_response_schema(row=row)

        except IntegrityError as e:
            await self._db.rollback()
            error_message = 'Something went wrong'

            if 'name' in str(e.orig):
                error_message = 'This name already exists.'
            elif 'email' in str(e.orig):
                error_message = 'This email already exists.'

            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=error_message
            )

        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e)
            )

        finally:
            await self._db.rollback()


    async def get_user(self, user_id):
        query = select(User).where(User.id == user_id)
        user = await self._db.scalar(query)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'User with id {user_id} not found'
            )

        return self._get_response_schema(model=user)


    async def update_user(self, user_id, data):
        pass

    async def delete_user(self, user_id):
        pass

    def _hash_password(self, password: str) -> str:
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')

    def _check_password(self, password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))


class GenderRepository(BaseRepository):
    response_schema = GenderResponseSchema

    def __init__(self, db):
        self._db = db

    async def create_gender(self, data):
        try:
            query = insert(Gender).values(name=data.name).returning(Gender)
            row = await self._db.execute(query)
            await self._db.commit()

            return self._get_response_schema(row=row)

        except IntegrityError as e:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f'Gender already exists'
            )
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e)
            )

        finally:
            await self._db.rollback()

    async def get_gender(self, gender_id):
        query = select(Gender).where(Gender.id == gender_id)
        gender = await self._db.scalar(query)

        if not gender:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Gender with id {gender} not found'
            )

        return self._get_response_schema(model=gender)

    async def update_gender(self, user_id, data):
        pass

    async def delete_gender(self, user_id):
        pass


class TopicRepository(BaseRepository):
    def __init__(self, db):
        self.db = db

    async def create_topic(self, user_id, data):
        pass

    async def get_topic(self, user_id):
        pass

    async def update_topic(self, user_id, data):
        pass

    async def delete_topic(self, user_id):
        pass



