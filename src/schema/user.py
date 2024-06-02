from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator

from src.schema.mongo import PyObjectId


# These fields are present in all kinds of user models.
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


# This model will contain fields from database.
class UserDB(User):
    hashed_password: str

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
    )


class UserIn(UserBase):
    password: str

    @field_validator("password")
    def validate_password(cls, v: str) -> str:
        if v.strip() == "":
            raise ValueError("password must not be empty")
        return v


class UserManyResponse(BaseModel):
    records: List[UserBase]
