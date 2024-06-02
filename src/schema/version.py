from pydantic import BaseModel, Field


class Version(BaseModel):
    app_name: str = Field(..., alias="appName")
    api: str
