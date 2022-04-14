from abc import ABC, abstractmethod
from typing import Optional, cast

import shortuuid

from calculator.domain import (
    Operator,
    OperationNotFoundError,
    OperationRepository,
    Number,
    Operation
)

from .operation_command_model import OperationCreateModel
from .operation_query_model import OperationReadModel


class OperationCommandUseCaseUnitOfWork(ABC):
    """OperationCommandUseCaseUnitOfWork defines an interface based on Unit of Work pattern."""

    operation_repository: OperationRepository

    @abstractmethod
    def begin(self):
        raise NotImplementedError

    @abstractmethod
    def commit(self):
        raise NotImplementedError

    @abstractmethod
    def rollback(self):
        raise NotImplementedError


class OperationCommandUseCase(ABC):
    """OperationCommandUseCase defines a command usecase inteface related Operation entity."""

    @abstractmethod
    def create_operation(self, data: OperationCreateModel) -> Optional[OperationReadModel]:
        raise NotImplementedError

    @abstractmethod
    def delete_operation_by_id(self, id: str):
        raise NotImplementedError


class OperationCommandUseCaseImpl(OperationCommandUseCase):
    """OperationCommandUseCaseImpl implements a command usecases related Operation entity."""

    def __init__(
        self,
        uow: OperationCommandUseCaseUnitOfWork,
    ):
        self.uow: OperationCommandUseCaseUnitOfWork = uow

    def create_operation(self, data: OperationCreateModel) -> Optional[OperationReadModel]:
        try:
            uuid = shortuuid.uuid()
            operator = Operator(data.operator)
            frist_number = Number(data.first_number)
            second_number = Number(data.second_number)
            operation = Operation(id=uuid, operator=operator, first_number=frist_number, second_number=second_number)

            self.uow.operation_repository.create(operation)
            self.uow.commit()

            created_operation = self.uow.operation_repository.find_by_id(uuid)
        except:
            self.uow.rollback()
            raise

        return OperationReadModel.from_entity(cast(Operation, created_operation))

    def delete_operation_by_id(self, id: str):
        try:
            existing_operation = self.uow.operation_repository.find_by_id(id)
            if existing_operation is None:
                raise OperationNotFoundError

            self.uow.operation_repository.delete_by_id(id)

            self.uow.commit()
        except:
            self.uow.rollback()
            raise