from pos.payment_method_picker.payment_method_picker import PaymentMethodPicker
from pos.payment_method_picker.payment_methods import PaymentMethods
from pos.product_picker.picked_product import PickedProduct
from pos.product_picker.product_picker import ProductPicker
from pos.uncategorized.payment import Payment


class Customer:
    def __init__(
        self, product_picker: ProductPicker, payment_method_picker: PaymentMethodPicker
    ):
        self.product_picker = product_picker
        self.payment_method_picker = payment_method_picker

        self.last_paid_amount: float = 0
        self.last_used_payment_method = PaymentMethods.NONE

    def pick_products(self) -> list[PickedProduct]:
        return self.product_picker.pick_products()

    def pay(self, amount: float) -> None:
        picked_payment_method = self.payment_method_picker.pick()

        picked_payment_method.pay(amount)

        self.last_paid_amount = amount
        self.last_used_payment_method = picked_payment_method.get_type()

    def get_last_payment(self) -> Payment:
        return Payment(self.last_paid_amount, self.last_used_payment_method)
