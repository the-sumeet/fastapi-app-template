from typing import Dict, List

from pydantic import BaseModel


class ManyResponse(BaseModel):
    records: List[Dict]
