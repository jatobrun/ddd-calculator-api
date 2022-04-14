class OperationNotFoundError(Exception):
    msg = "The operation does not exist."
    
    def __str__(self):
        return OperationNotFoundError.msg


class OperationsNotFoundError(Exception):
    msg = "No operations were found"
    
    def __str__(self):
        return OperationsNotFoundError.msg
    
