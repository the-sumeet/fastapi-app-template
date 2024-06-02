from kink import di
from motor.motor_asyncio import AsyncIOMotorClient

from src.core.config import Settings
from src.repository.user import UserRepository

di[Settings] = Settings()
di["MongoClient"] = lambda di: AsyncIOMotorClient(di[Settings].MONGO_DB_URL)
di[UserRepository] = lambda di: UserRepository(di["MongoClient"], di[Settings])
