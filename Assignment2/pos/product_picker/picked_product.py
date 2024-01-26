from pos.product.iproduct import IProduct


class PickedProduct:
    def __init__(self, product: IProduct, amount: int):
        self.product = product
        self.amount = amount

    def __repr__(self) -> str:
        return f"{self.amount}x {self.product.get_name()}"

    def get_product(self) -> IProduct:
        return self.product

    def get_amount(self) -> int:
        return self.amount

    def get_name(self) -> str:
        return self.product.get_name()

    def get_total_price(self) -> float:
        return round(self.product.get_price() * self.amount, 2)
