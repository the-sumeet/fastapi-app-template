from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.middleware.cors import CORSMiddleware

import app.di  # noqa
from app.create_app import create_app
from app.middleware.authentication import AuthMiddleware, authentication_error_handler

fatapi_app = create_app()

fatapi_app.add_middleware(
    middleware_class=AuthenticationMiddleware,
    backend=AuthMiddleware(),
    on_error=authentication_error_handler,
)

fatapi_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
