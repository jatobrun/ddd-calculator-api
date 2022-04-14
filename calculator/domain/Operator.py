from dataclasses import dataclass
from ...utils.Constants import Constants

@dataclass(init=False, eq=True, frozen=True)
class Operator:
    """ Operator represent a simple math operator as a value object """
    
    value: str
    
    def __init__(self, value: str):
        if self.is_not_valid_operator(value):
            raise ValueError(Constants.OPERATOR_ERROR)
        else:
            object.__setattr__(self, "value", value)
    
    def is_not_valid_operator(value:str) -> bool:
        return value not in Constants.OPERATORS