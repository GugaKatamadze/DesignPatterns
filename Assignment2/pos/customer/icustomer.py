from typing import Protocol

from pos.product_picker.picked_product import PickedProduct
from pos.uncategorized.payment import Payment


class ICustomer(Protocol):
    def pick_products(self) -> list[PickedProduct]:
        pass

    def pay(self, amount: float) -> None:
        pass

    def get_last_payment(self) -> Payment:
        pass
