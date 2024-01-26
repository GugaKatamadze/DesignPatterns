from typing import Protocol

from pos.cash_register.cash_register import CashRegister
from pos.customer.icustomer import ICustomer
from pos.repository.repository import Repository
from pos.uncategorized.payment import Payment
from pos.uncategorized.receipt import Receipt


class ICashier(Protocol):
    def take_order(self, customer: ICustomer) -> None:
        pass

    def get_receipt(self) -> Receipt:
        pass

    def close_receipt(self) -> None:
        pass

    def update_sales(self, cash_register: CashRegister, repository: Repository) -> None:
        pass

    def update_revenue(
        self, cash_register: CashRegister, repository: Repository, payment: Payment
    ) -> None:
        pass
