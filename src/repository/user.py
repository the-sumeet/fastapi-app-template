from typing import Optional

from fastapi import status
from fastapi.exceptions import HTTPException
from jose import JWTError, jwt
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import DuplicateKeyError

from src.core.config import Settings
from src.repository.mongo import AbstractMongoRepository, SearchMixin, WriteMixin
from src.schema.auth import EmailPassword
from src.schema.token import TokenData
from src.schema.user import UserIn, CreateUserDb, UserDB, User
from src.utils.auth import get_password_hash, verify_password

COLLECTION_NAME = "users"


class UserRepository(AbstractMongoRepository, SearchMixin, WriteMixin):
    def __init__(self, client: AsyncIOMotorClient, settings: Settings):
        db = client.get_database(settings.MONGO_DB_NAME)
        self.collection = db.get_collection(COLLECTION_NAME)
        self.model = User
        self.settings = settings
        super().__init__(client=client)

    async def create_user(self, new_user: UserIn) -> User:

        hashed_password = get_password_hash(new_user.password)
        db_user = CreateUserDb(**new_user.dict(), hashed_password=hashed_password)
        try:
            res = await self.create(db_user)
        except DuplicateKeyError:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="user with this email already exists.",
            )
        return res

    async def authenticate_user(self, creds: EmailPassword) -> UserDB:
        user = await self.get_one(filters={"email": creds.email}, return_model=UserDB)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "user not found"}
            )
        if not verify_password(creds.password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"msg": "invalid credentials"},
            )
        return user

    async def get_current_user(self, token: str) -> User | None:
        """Get user from token"""
        try:
            payload = jwt.decode(
                token, self.settings.SECRET_KEY, algorithms=[self.settings.ALGORITHM]
            )
            email: Optional[str] = payload.get("sub")
            if email is None:
                return None
            token_data = TokenData(email=email)
        except JWTError:
            return None
        user = await self.get_one(
            filters={"email": token_data.email}, return_model=User
        )
        return user
