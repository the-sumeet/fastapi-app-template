from typing import Optional, List

from pydantic import BaseModel, Field, ConfigDict

from app.schema.mongo import PyObjectId
from pydantic import field_validator


class UserBase(BaseModel):
    name: str = Field(...)
    email: str = Field(...)
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
    )


class User(UserBase):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
    )


class CreateUserDb(UserBase):
    hashed_password: str


class DbUser(User):
    hashed_password: str

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
    )


class CreateUser(UserBase):
    password: str

    @field_validator('password')
    @classmethod
    def validate_password(cls, v: str) -> str:
        if v.strip() == "":
            raise ValueError('password must not be empty')
        return v


class UserManyResponse(BaseModel):
    records: List[UserBase]
