from pos.payment_method_picker.payment_methods import PaymentMethods


class Cash:
    def pay(self, amount: float) -> None:
        print(f"Customer paid {amount} with cash")

    def get_type(self) -> PaymentMethods:
        return PaymentMethods.CASH
