from abc import ABC, abstractmethod
from typing import List, Optional

from calculator.domain import OperationNotFoundError, OperationsNotFoundError

from .operation_query_model import OperationReadModel
from .operation_query_service import OperationQueryService


class OperationQueryUseCase(ABC):
    """OperationQueryUseCase defines a query usecase inteface related Operation entity."""

    @abstractmethod
    def fetch_operation_by_id(self, id: str) -> Optional[OperationReadModel]:
        raise NotImplementedError

    @abstractmethod
    def fetch_operations(self) -> List[OperationReadModel]:
        raise NotImplementedError


class OperationQueryUseCaseImpl(OperationQueryUseCase):
    """OperationQueryUseCaseImpl implements a query usecases related Operation entity."""

    def __init__(self, operation_query_service: OperationQueryService):
        self.operation_query_service: OperationQueryService = operation_query_service

    def fetch_operation_by_id(self, id: str) -> Optional[OperationReadModel]:
        try:
            operation = self.operation_query_service.find_by_id(id)
            if operation is None:
                raise OperationNotFoundError
        except:
            raise

        return operation

    def fetch_operations(self) -> List[OperationReadModel]:
        try:
            operations = self.operation_query_service.find_all()
            if operations is None:
                raise OperationsNotFoundError
        except:
            raise 

        return operations