from typing import Annotated

from fastapi import APIRouter, Depends

from src.api.routes.auth import router as auth_router
from src.api.routes.users import router as users_router
from src.deps import current_user
from src.schema.user import UserBase

router = APIRouter()

router.include_router(users_router, prefix="/users", tags=["users"])
router.include_router(auth_router, prefix="/auth", tags=["auth"])


@router.get("/")
async def home(user: Annotated[UserBase, Depends(current_user)]):
    return {"msg": f"Hello {user.name}"}
