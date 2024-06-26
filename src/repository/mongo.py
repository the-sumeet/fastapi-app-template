import abc
from typing import Dict, Optional, Type, TypeVar, Awaitable, Any

from motor.core import AgnosticClient
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
from pymongo.collection import Collection
from pymongo.results import InsertOneResult

from src.schema.response import ManyResponse

T = TypeVar("T", bound=BaseModel)

class AbstractMongoRepository(abc.ABC):
    client: AgnosticClient
    collection: Collection
    model: Type[BaseModel]

    def __init__(self, client: AgnosticClient):
        self.client = client


class SearchMixin:
    collection: Collection
    model: Type[BaseModel]

    async def get_many(self, filters: Optional[Dict] = None) -> ManyResponse:
        records = await self.collection.find(filters).to_list(1000)
        return ManyResponse(records=records)

    async def get_one(
        self,
        record_id: Optional[str] = None,
        filters: Optional[Dict] = None,
        return_model: Optional[Type[T]] = None,
    ) -> T | Dict | None:

        if not record_id and not filters:
            return None

        if record_id is not None:
            filters = {"_id": record_id}

        record: Awaitable[Any] = await self.collection.find_one(filters)

        if record is None:
            return record

        return return_model.parse_obj(record) if return_model else record


class WriteMixin:
    model: Type[BaseModel]
    collection: Collection

    async def create(
        self, record: BaseModel | Dict, return_model: Optional[Type[T]] = None,
    ) -> Dict | T:

        if isinstance(record, BaseModel):
            new_record: InsertOneResult = await self.collection.insert_one(
                record.model_dump(by_alias=True, exclude={"id"})
            )
        else:
            new_record = await self.collection.insert_one(record)
        created_record = await self.collection.find_one({"_id": new_record.inserted_id})

        try:
            if return_model:
                return return_model.parse_obj(created_record)

            return created_record
        except Exception:
            return created_record
