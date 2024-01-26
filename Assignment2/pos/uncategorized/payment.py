from pos.payment_method_picker.payment_methods import PaymentMethods


class Payment:
    def __init__(self, amount: float, payment_method: PaymentMethods):
        self.amount = amount
        self.payment_method = payment_method

    def get_amount(self) -> float:
        return self.amount

    def get_payment_method(self) -> PaymentMethods:
        return self.payment_method
