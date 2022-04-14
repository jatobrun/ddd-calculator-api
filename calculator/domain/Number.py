from dataclasses import dataclass
from ...utils.Constants import Constants

@dataclass(init=False, eq=True, frozen=True)
class Number:
    """ NUmber represent a positive number as a value object """
    
    value: int
    
    def __init__(self, value: str):
        value = self.convert_string_number_to_integer(value)
        
        if self.is_positive_number(value):
            object.__setattr__(self, "value", value)
        else:
            raise ValueError(Constants.NUMBER_ERROR_MESSAGE)
            
    
    def convert_string_number_to_integer(self, value:str) -> int:
        """Converts a string number into a integer number (casting)
        Args:
            number (str): the string number that I want to convert into a number
        Raises:
            BusinessRulesValidationException: If its not a invalid string number
        Returns:
            int: the number value in the string arg
        """
        if not(value.isdecimal()):
            raise ValueError(Constants.NUMBER_ERROR_MESSAGE)
        return int(value)

    def is_positive_number(value:int) -> bool:
        return value >= 0