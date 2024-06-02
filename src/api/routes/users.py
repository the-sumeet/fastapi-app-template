from fastapi import APIRouter, Body, Depends, status
from kink import di

from src.repository.user import UserRepository
from src.schema.user import CreateUser, User, UserManyResponse

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
