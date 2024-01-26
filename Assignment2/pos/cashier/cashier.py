from pos.cash_register.cash_register import CashRegister
from pos.customer.icustomer import ICustomer
from pos.payment_method.payment_method_to_str_adapter import (
    CardToStrAdapter,
    CashToStrAdapter,
)
from pos.repository.repository import Repository
from pos.uncategorized.payment import Payment
from pos.uncategorized.receipt import Receipt


class Cashier:
    def __init__(self) -> None:
        self.receipt = Receipt()

    def take_order(self, customer: ICustomer) -> None:
        for picked in customer.pick_products():
            self.receipt.add_items(picked.get_product(), picked.get_amount())

    def get_receipt(self) -> Receipt:
        return self.receipt

    def close_receipt(self) -> None:
        self.receipt.close()

    def update_sales(self, cash_register: CashRegister, repository: Repository) -> None:
        for product, amount in self.receipt.get_products().items():
            for _ in range(0, amount):
                cash_register.add_sale(product.get_name())
                repository.add_sale(product)

    def update_revenue(
        self, cash_register: CashRegister, repository: Repository, payment: Payment
    ) -> None:
        payment_method = CardToStrAdapter(CashToStrAdapter()).adapt(
            payment.get_payment_method()
        )

        cash_register.add_revenue(payment.get_amount(), payment_method)
        repository.add_revenue(payment.get_amount(), payment_method)
