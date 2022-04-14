from pydantic import BaseModel, Field

class OperationCreateModel(BaseModel):
    
    operator: str = Field(example='+, /, *, -')
    first_number: str = Field(example='987654321')
    second_number: str = Field(example='987654321')