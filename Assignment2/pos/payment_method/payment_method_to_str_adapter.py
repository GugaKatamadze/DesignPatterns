from typing import Protocol

from pos.payment_method_picker.payment_methods import PaymentMethods


class PaymentMethodToStrAdapter(Protocol):
    def adapt(self, payment_type: PaymentMethods) -> str:
        pass


class NoAdapter:
    def adapt(self, payment_type: PaymentMethods) -> str:
        raise Exception


class CardToStrAdapter:
    def __init__(self, next_adapter: PaymentMethodToStrAdapter = NoAdapter()) -> None:
        self.next_adapter = next_adapter

    def adapt(self, payment_type: PaymentMethods) -> str:
        if payment_type == PaymentMethods.CARD:
            return "Card"

        return self.next_adapter.adapt(payment_type)


class CashToStrAdapter:
    def __init__(self, next_adapter: PaymentMethodToStrAdapter = NoAdapter()) -> None:
        self.next_adapter = next_adapter

    def adapt(self, payment_type: PaymentMethods) -> str:
        if payment_type == PaymentMethods.CASH:
            return "Cash"

        return self.next_adapter.adapt(payment_type)
