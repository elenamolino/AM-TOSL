from pydantic import BaseModel


class EvaluationResult(BaseModel):
    clause_id: str
    original_text: str
    back_translated: str
    semantic_sim: float
