from datetime import timedelta

from fastapi import APIRouter, Body, Depends
from kink import di

from src.core.config import Settings
from src.repository.user import UserRepository
from src.schema.auth import EmailPassword
from src.schema.token import Token
from src.schema.user import UserDB
from src.utils.auth import create_access_token

router = APIRouter()


@router.post("/login")
async def login(
    creds: EmailPassword = Body(),
    repo: UserRepository = Depends(lambda: di[UserRepository]),
    settings: Settings = Depends(lambda: di[Settings]),
) -> Token:
    user: UserDB = await repo.authenticate_user(creds)
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")
