from typing import Protocol

from spore.evolution.evolution import Evolution
from spore.move.move_result import MoveResult


class Move(Protocol):
    def move(
        self, evolution: Evolution, evolution_level: int, stamina: int
    ) -> MoveResult:
        pass
