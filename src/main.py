from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.middleware.cors import CORSMiddleware

import src.di  # noqa
from src.create_app import create_app
from src.middleware.authentication import AuthMiddleware, authentication_error_handler

app = create_app()

app.add_middleware(
    middleware_class=AuthenticationMiddleware,
    backend=AuthMiddleware(),
    on_error=authentication_error_handler,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
