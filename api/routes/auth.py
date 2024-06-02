from datetime import timedelta

from fastapi import APIRouter
from fastapi import Depends, Body

from app.core.config import Settings
from app.repository.user import UserRepository
from app.schema.auth import EmailPassword
from app.schema.token import Token
from app.schema.user import UserManyResponse, CreateUser, User, DbUser
from kink import di
from fastapi import status
from app.utils.auth import get_password_hash, create_access_token

router = APIRouter()


@router.post("/login")
async def login(
        creds: EmailPassword = Body(),
        repo: UserRepository = Depends(lambda: di[UserRepository]),
        settings: Settings = Depends(lambda: di[Settings]),
) -> Token:
    user: DbUser = await repo.authenticate_user(creds)
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")
