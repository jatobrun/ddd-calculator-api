from abc import ABC, abstractmethod
from ast import Delete
from typing import List, Optional

from calculator.domain.Operation import Operation


class OperationRepository(ABC):
    """OperationRepository defines a repository interface for Operation entity."""
    
    @abstractmethod
    def create(self, book: Operation) -> Optional[Operation]:
        raise NotImplementedError
    
    @abstractmethod
    def delete_by_id(self, id: str):
        raise NotImplementedError
    
    @abstractmethod
    def search_by_id(self, id: str) -> Optional[Operation]:
        raise NotImplementedError