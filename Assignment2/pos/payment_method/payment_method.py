from typing import Protocol

from pos.payment_method_picker.payment_methods import PaymentMethods


class PaymentMethod(Protocol):
    def pay(self, amount: float) -> None:
        pass

    def get_type(self) -> PaymentMethods:
        pass
