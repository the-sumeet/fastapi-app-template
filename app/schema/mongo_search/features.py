import abc
from dataclasses import dataclass
from typing import List, Type, Any

from pydantic import BaseModel

from app.schema.mongo_search.params import ParamsBase


class SearchFeatureConfig:
    pass


class SearchFeature(abc.ABC):
    params: ParamsBase
    config: SearchFeatureConfig

    @abc.abstractmethod
    def build_q(self, *args, **kwargs):
        raise NotImplementedError


class MatchField(SearchFeature):
    @dataclass
    class Config(SearchFeatureConfig):
        field: str
        param: str
        value: Any

    config: Config

    def build_q(self, params: ParamsBase, **kwargs):
        value = self.config.value
        if value is None:
            value = getattr(params, self.config.param)

        if isinstance(value, list):
            return {self.config.field: {'$in': value}}

        return {self.config.field: value}
