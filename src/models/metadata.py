from typing import Literal
from pydantic import BaseModel
from src.config import ALL_ACTIONS

ClauseType = Literal[
    "permission",
    "prohibition",
    "obligation",
    "dispute resolution",
    "liability",
    "other",
]

Party = Literal["customer", "provider", "both", "unspecified"]

Action = Literal[tuple(ALL_ACTIONS)]  # type: ignore[valid-type]


class ClauseMetadata(BaseModel):
    clause_id: str
    clause_text: str
    type: ClauseType
    party: Party
    action: Action
    asset: str
