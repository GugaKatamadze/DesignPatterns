from pos.payment_method_picker.payment_methods import PaymentMethods


class Thanks:
    def pay(self, amount: float) -> None:
        print("Customer is extremely grateful")

    def get_type(self) -> PaymentMethods:
        return PaymentMethods.THANKS
