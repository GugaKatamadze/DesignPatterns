from typing import Protocol


class IProduct(Protocol):
    def get_name(self) -> str:
        pass

    def get_price(self) -> float:
        pass
