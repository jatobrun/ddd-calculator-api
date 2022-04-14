from ast import Num
from typing import Optional

from .Number import Number
from .Operator import Operator

class Operation:
    """Operation represents your aritmetic operation of positive number as an entity."""
    
    def __init__(
        self,
        id: str,
        operator: Operator,
        first_number: Number,
        second_number: Number,
        result: int,
        created_at: Optional[int] = None     
    ):
        self.id: str = id
        self.operator: Operator = operator
        self.first_number: Number = first_number
        self.second_number: Number = second_number
        self.result: int = result
        created_at: Optional[int] = created_at
        
    def __eq__(self, o: object) -> bool:
        if isinstance(o, Operation):
            return self.id == o.id

        return False
         
        