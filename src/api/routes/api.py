from typing import Annotated

from fastapi import APIRouter, Depends
from kink import di

from src.api.routes.auth import router as auth_router
from src.api.routes.users import router as users_router
from src.core.config import Settings
from src.deps import current_user
from src.schema.user import UserBase
from src.schema.version import Version

router = APIRouter()

router.include_router(users_router, prefix="/users", tags=["users"])
router.include_router(auth_router, prefix="/auth", tags=["auth"])


@router.get("/version", response_model=Version)
async def home(
        settings: Settings = Depends(lambda: di[Settings])
):
    return Version(appName=settings.APP_NAME, api=settings.API_PREFIX)


@router.get("/")
async def home(user: Annotated[UserBase, Depends(current_user)]):
    return {"msg": f"Hello {user.name}"}
