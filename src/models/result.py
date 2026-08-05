from pydantic import BaseModel, Field
from src.models.contract import Contract
from src.models.metadata import ClauseMetadata
from src.models.turtle import CorrectedTurtle
from src.models.analysis import ClauseAnalysis
from src.models.evaluation import EvaluationResult


class PipelineResult(BaseModel):
    contract: Contract
    metadata: list[ClauseMetadata] = Field(default_factory=list)
    turtle_files: list[CorrectedTurtle] = Field(default_factory=list)
    analysis: list[ClauseAnalysis] = Field(default_factory=list)
    evaluation: list[EvaluationResult] = Field(default_factory=list)
