from pydantic import BaseModel, Field


class EmailPassword(BaseModel):
    email: str = Field(...)
    password: str = Field(...)
