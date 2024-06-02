import http

from fastapi.responses import JSONResponse
from kink import inject
from starlette.authentication import (
    AuthCredentials,
    AuthenticationBackend,
    AuthenticationError,
    BaseUser,
)
from starlette.requests import HTTPConnection

from app.core.config import Settings
from app.repository.user import UserRepository


def authentication_error_handler(conn: HTTPConnection, exc: AuthenticationError):
    return JSONResponse(
        status_code=http.HTTPStatus.UNAUTHORIZED, content={"msg": str(exc)}
    )


class AuthMiddleware(AuthenticationBackend):
    def __init__(
        self,
    ):
        super().__init__()

    @inject
    async def authenticate(
        self, conn: HTTPConnection, user_repo: UserRepository, settings: Settings
    ) -> tuple[AuthCredentials, BaseUser] | None:
        if conn.url.path not in settings.SKIP_AUTH_ROUTES:
            token = conn.headers.get("Authorization")
            if token in [None, ""]:
                raise AuthenticationError("No auth token found")
            user = await user_repo.get_current_user(token=token)
            if not user:
                raise AuthenticationError("Invalid token")
            conn.state.user = user
        return
