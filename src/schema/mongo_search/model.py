from typing import List

from pydantic import BaseModel

from src.schema.mongo_search.features import SearchFeature
from src.schema.mongo_search.params import ParamsBase


class SearchModel(BaseModel):
    params: ParamsBase
    features: List[SearchFeature]
