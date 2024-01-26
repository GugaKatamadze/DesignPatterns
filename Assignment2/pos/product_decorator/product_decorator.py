from pos.product.iproduct import IProduct


class ProductDecorator:
    def __init__(self, product: IProduct):
        self.product = product

    def __repr__(self) -> str:
        return self.product.__repr__()

    def get_name(self) -> str:
        return self.product.get_name()

    def get_price(self) -> float:
        return self.product.get_price()
