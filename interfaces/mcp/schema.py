from pydantic import BaseModel


class EquipmentInfo(BaseModel):
    name: str
    x: int
    y: int
    z: int


class ValidationReport(BaseModel):
    violations: dict
