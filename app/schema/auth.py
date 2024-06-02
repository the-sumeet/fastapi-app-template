from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator

from app.schema.mongo import PyObjectId


class EmailPassword(BaseModel):
    email: str = Field(...)
    password: str = Field(...)
