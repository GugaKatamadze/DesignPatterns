from pos.product.iproduct import IProduct


class Receipt:
    def __init__(self) -> None:
        self.products: dict[IProduct, int] = dict()

    def get_products(self) -> dict[IProduct, int]:
        return self.products

    def add_item(self, product: IProduct) -> None:
        if product not in self.products:
            self.products[product] = 0

        self.products[product] += 1

    def add_items(self, product: IProduct, amount: int) -> None:
        for _ in range(0, amount):
            self.add_item(product)

    def get_total_price(self) -> float:
        return sum(
            product.get_price() * amount for product, amount in self.products.items()
        )

    def close(self) -> None:
        self.products.clear()
