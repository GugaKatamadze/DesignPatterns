from typing import Protocol

from pos.payment_method.payment_method import PaymentMethod


class PaymentMethodPicker(Protocol):
    def pick(self) -> PaymentMethod:
        pass
