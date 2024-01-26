class RevenueInfo:
    def __init__(self, payment_method: str, amount: float):
        self.payment_method = payment_method
        self.amount = round(amount, 2)

    def __repr__(self) -> str:
        return f"{self.payment_method} {self.amount}"

    def get_payment_method(self) -> str:
        return self.payment_method

    def get_amount(self) -> float:
        return self.amount
