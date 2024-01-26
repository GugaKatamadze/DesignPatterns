class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __repr__(self) -> str:
        return self.name

    def get_name(self) -> str:
        return self.name

    def get_price(self) -> float:
        return round(self.price, 2)
