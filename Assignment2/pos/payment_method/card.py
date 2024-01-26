from pos.payment_method_picker.payment_methods import PaymentMethods


class Card:
    def pay(self, amount: float) -> None:
        print(f"Customer paid {amount} with card")

    def get_type(self) -> PaymentMethods:
        return PaymentMethods.CARD
