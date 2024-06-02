from fastapi import APIRouter
from fastapi import Depends, Body
from app.repository.user import UserRepository
from app.schema.user import UserManyResponse, CreateUser, User
from kink import di
from fastapi import status
from app.utils.auth import get_password_hash

router = APIRouter()


@router.get("", response_model=UserManyResponse)
async def get_users(
    repo: UserRepository = Depends(lambda: di[UserRepository]),
):
    """
    :return: List of movies
    """
    return await repo.get_many()


@router.post("/register", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(
        user: CreateUser = Body(),
        repo: UserRepository = Depends(lambda: di[UserRepository]),
) -> User:
    return await repo.create_user(user)
