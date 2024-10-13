from pydantic import BaseModel, Field


class GenderCreateSchema(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)


class GenderResponseSchema(BaseModel):
    id: int
    name: str