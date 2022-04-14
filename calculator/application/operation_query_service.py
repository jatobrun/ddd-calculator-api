from abc import ABC, abstractmethod
from typing import List, Optional

from .operation_query_model import OperationReadModel


class OperationQueryService(ABC):
    """OperationQueryService defines a query service inteface related Operation entity."""

    @abstractmethod
    def find_by_id(self, id: str) -> Optional[OperationReadModel]:
        raise NotImplementedError

    @abstractmethod
    def find_all(self) -> List[OperationReadModel]:
        raise NotImplementedError
