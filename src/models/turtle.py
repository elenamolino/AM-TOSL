from pydantic import BaseModel, Field


class TurtleOutput(BaseModel):
    clause_id: str
    clause_text: str
    ttl: str


class ValidationViolation(BaseModel):
    focus_node: str = ""
    result_path: str = ""
    value_node: str = ""
    message: str = ""


class ValidationReport(BaseModel):
    conforms: bool
    violations: list[ValidationViolation] = Field(default_factory=list)


class CorrectedTurtle(BaseModel):
    clause_id: str
    clause_text: str = ""
    ttl: str
    repair_rounds: int
    final_report: ValidationReport
