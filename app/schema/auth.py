from typing import Optional, List

from pydantic import BaseModel, Field, ConfigDict

from app.schema.mongo import PyObjectId
from pydantic import field_validator


class EmailPassword(BaseModel):
    email: str = Field(...)
    password: str = Field(...)

