from pos.product.iproduct import IProduct
from pos.product_decorator.product_decorator import ProductDecorator


class Discount(ProductDecorator):
    def __init__(self, discount: int, product: IProduct):
        super().__init__(product)

        self.discount = discount

    def get_price(self) -> float:
        return round((1 - self.discount / 100) * self.product.get_price(), 2)
