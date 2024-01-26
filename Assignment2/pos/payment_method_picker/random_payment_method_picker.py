import random

from pos.payment_method.payment_method import PaymentMethod
from pos.payment_method_picker.payment_method_selector import CardSelector, CashSelector
from pos.payment_method_picker.payment_methods import PaymentMethods


class RandomPaymentMethodPicker:
    def pick(self) -> PaymentMethod:
        payment_methods = [PaymentMethods.CARD, PaymentMethods.CASH]

        random_payment_method = payment_methods[
            random.randint(0, len(payment_methods) - 1)
        ]

        payment_method_selector = CardSelector(CashSelector())

        return payment_method_selector.select(random_payment_method)
