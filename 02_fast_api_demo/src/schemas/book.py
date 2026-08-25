from pydantic import BaseModel, ConfigDict, Field


class BookBase(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    author: str = Field(min_length=1, max_length=120)
    description: str | None = None


class BookCreate(BookBase):
    pass


class BookResponse(BookBase):
    id: int

    model_config = ConfigDict(from_attributes=True)