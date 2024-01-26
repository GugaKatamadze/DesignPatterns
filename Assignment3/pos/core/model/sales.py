class Sales:
    def __init__(self, n_receipts: int, revenue: float) -> None:
        self.n_receipts = n_receipts
        self.revenue = revenue

    def get_n_receipts(self) -> int:
        return self.n_receipts

    def get_revenue(self) -> float:
        return self.revenue
