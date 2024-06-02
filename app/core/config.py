from typing import List

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_PREFIX: str = "/api/v1"
    APP_NAME: str = "FastAPI App"
    MONGO_DB_URL: str

    # Auth
    SECRET_KEY: str = "3a8b2782f8ed4db805f3dc0f3c2798a2f5030f29e4e4d3f70cb281c452b1181a"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1000

    SKIP_AUTH_ROUTES: List[str] = [
        f"{API_PREFIX}/",
        f"{API_PREFIX}/docs",
        f"{API_PREFIX}/openapi.json",
        f"{API_PREFIX}/auth/login",
        f"{API_PREFIX}/users/register",
    ]
