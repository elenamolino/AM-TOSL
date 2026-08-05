from pydantic import BaseModel, Field


class Clause(BaseModel):
    id: str
    text: str


class Contract(BaseModel):
    provider: str
    source: str
    title: str
    date: str
    description: str = ""
    clauses: list[Clause] = Field(default_factory=list)
