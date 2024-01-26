from typing import Protocol

from pos.product_picker.picked_product import PickedProduct


class ProductPicker(Protocol):
    def pick_products(self) -> list[PickedProduct]:
        pass
