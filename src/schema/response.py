from typing import Dict, List, Type

from pydantic import BaseModel



class ManyResponse(BaseModel):
    records: List[Type[BaseModel]]
