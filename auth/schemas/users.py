from typing import Optional

from pydantic import BaseModel, Field, EmailStr, SecretStr


class UserCreateSchema(BaseModel):
    telegram_id: Optional[int] = None

    name: str = Field(..., min_length=3, max_length=50)
    email: EmailStr = Field(...)
    password: SecretStr = Field(..., min_length=6)

    gender_id: int


class UserResponseSchema(BaseModel):
    id: int
    telegram_id: int = None

    name: str
    email: str
    gender_id: int
    is_active: bool
