from pydantic import BaseModel, Field


class TopicCreateSchema(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
