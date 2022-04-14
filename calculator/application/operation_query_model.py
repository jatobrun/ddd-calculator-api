from typing import cast

from pydantic import BaseModel, Field

from calculator.domain.Operation import Operation


class OperationReadModel(BaseModel):
    """OperationReadModel represents data structure as a read model."""

    id: str = Field(example="vytxeTZskVKR7C7WgdSP3d")
    operator: str = Field(example="+")
    first_number: str = Field(example="10")
    second_number: str = Field(example="12")
    created_at: int = Field(example=1136214245000)

    class Config:
        orm_mode = True

    @staticmethod
    def from_entity(operation: Operation) -> "OperationReadModel":
        return OperationReadModel(
            id=operation.id,
            operator=operation.operator.value,
            first_number=operation.first_number.value,
            second_number=operation.second_number.value,
            created_at=cast(int, operation.created_at),
        )