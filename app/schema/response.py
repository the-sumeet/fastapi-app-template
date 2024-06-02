from typing import List, Dict

from pydantic import BaseModel


class ManyResponse(BaseModel):
    records: List[Dict]
