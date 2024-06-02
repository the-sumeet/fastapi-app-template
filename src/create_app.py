from fastapi import FastAPI
from kink import inject

from src.api.routes.api import router
from src.core.config import Settings


@inject()
def create_app(settings: Settings) -> FastAPI:

    fastapi_app = FastAPI(
        title=settings.APP_NAME,
        openapi_url=f"{settings.API_PREFIX}/openapi.json",
        docs_url=f"{settings.API_PREFIX}/docs",
    )
    fastapi_app.include_router(router, prefix=settings.API_PREFIX)
    return fastapi_app
