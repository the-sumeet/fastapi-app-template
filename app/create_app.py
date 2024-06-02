from fastapi import FastAPI

from app.core.config import Settings
from api.routes.api import router


from kink import inject

@inject()
def create_app(settings: Settings) -> FastAPI:

    app = FastAPI(
        title=settings.APP_NAME,
        openapi_url=f"{settings.API_PREFIX}/openapi.json",
        docs_url=f"{settings.API_PREFIX}/docs",
    )
    app.include_router(router, prefix=settings.API_PREFIX)
    return app
