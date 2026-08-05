from typing import Optional
from pydantic import BaseModel, Field


class DeonticEntry(BaseModel):
    id: str = ""
    actions: list[str] = Field(default_factory=list)
    targets: list[str] = Field(default_factory=list)
    assignee: Optional[str] = None
    assigner: Optional[str] = None
    description: Optional[str] = None


class DeonticStatus(BaseModel):
    total_rules: int = 0
    duties: list[DeonticEntry] = Field(default_factory=list)
    permissions: list[DeonticEntry] = Field(default_factory=list)
    prohibitions: list[DeonticEntry] = Field(default_factory=list)


class ClauseAnalysis(BaseModel):
    clause_id: str
    deontic: DeonticStatus = Field(default_factory=DeonticStatus)
    unfair_terms: dict[str, list[dict]] = Field(default_factory=dict)
