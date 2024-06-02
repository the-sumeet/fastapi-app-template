from typing import List, Optional

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_PREFIX: str = "/api/v1"
    APP_NAME: str = "FastAPI App"
    MONGO_DB_URL: Optional[str] = None
    MONGO_DB_NAME: Optional[str] = None

    # Auth
    SECRET_KEY: str = "super_secret_key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1000

    SKIP_AUTH_ROUTES: List[str] = [
        f"{API_PREFIX}/",
        f"{API_PREFIX}/docs",
        f"{API_PREFIX}/openapi.json",
        f"{API_PREFIX}/auth/login",
        f"{API_PREFIX}/users/register",
    ]
