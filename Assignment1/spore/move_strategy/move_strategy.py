from typing import Protocol

from spore.evolution.evolution import Evolution
from spore.move.move_result import MoveResult


class MoveStrategy(Protocol):
    def move(self, stamina: int, evolutions: dict[Evolution, int]) -> MoveResult:
        pass
