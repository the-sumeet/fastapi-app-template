import abc
from typing import List

from pydantic import BaseModel

from app.schema.mongo_search.features import SearchFeature
from app.schema.mongo_search.params import ParamsBase


class SearchModel(BaseModel):
    params: ParamsBase
    features: List[SearchFeature]
