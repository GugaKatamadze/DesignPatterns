from pos.product.iproduct import IProduct


class PackOfProducts:
    def __init__(self) -> None:
        self.products: list[IProduct] = list()

    def __repr__(self) -> str:
        return self.get_name()

    def add_product(self, product: IProduct) -> None:
        self.products.append(product)

    def add_products(self, product: IProduct, amount: int) -> None:
        for _ in range(0, amount):
            self.add_product(product)

    def get_price(self) -> float:
        return round(sum(product.get_price() for product in self.products), 2)

    def get_name(self) -> str:
        return f"Pack of {len(self.products)} {self.products[0].get_name()}s"
