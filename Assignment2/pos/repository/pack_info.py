class PackInfo:
    def __init__(self, name: str, amount: int, discount: int):
        self.name = name
        self.amount = amount
        self.discount = discount

    def __repr__(self) -> str:
        return f"{self.discount}% discount on a {self.amount} pack of {self.name}"

    def get_name(self) -> str:
        return self.name

    def get_amount(self) -> int:
        return self.amount

    def get_discount(self) -> int:
        return self.discount
