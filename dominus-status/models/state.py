from pydantic import BaseModel
from typing import Literal

class StateModel(BaseModel):
    state: Literal["primary", "secondary", "noset"]
    hostname: str 