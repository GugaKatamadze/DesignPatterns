from typing import Protocol

from pos.customer.icustomer import ICustomer
from pos.repository.repository import Repository


class CustomerFactory(Protocol):
    def create(self, repository: Repository) -> ICustomer:
        pass
