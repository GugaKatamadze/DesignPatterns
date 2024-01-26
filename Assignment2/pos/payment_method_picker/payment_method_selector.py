from typing import Protocol

from pos.payment_method.card import Card
from pos.payment_method.cash import Cash
from pos.payment_method.payment_method import PaymentMethod
from pos.payment_method.thanks import Thanks
from pos.payment_method_picker.payment_methods import PaymentMethods


class PaymentMethodSelector(Protocol):
    def select(self, payment_method: PaymentMethods) -> PaymentMethod:
        pass


class NoSelector:
    def select(self, payment_method: PaymentMethods) -> PaymentMethod:
        return Thanks()


class CardSelector:
    def __init__(self, next_selector: PaymentMethodSelector = NoSelector()):
        self.next_selector = next_selector

    def select(self, payment_method: PaymentMethods) -> PaymentMethod:
        if payment_method is PaymentMethods.CARD:
            return Card()
        else:
            return self.next_selector.select(payment_method)


class CashSelector:
    def __init__(self, next_selector: PaymentMethodSelector = NoSelector()):
        self.next_selector = next_selector

    def select(self, payment_method: PaymentMethods) -> PaymentMethod:
        if payment_method is PaymentMethods.CASH:
            return Cash()
        else:
            return self.next_selector.select(payment_method)
