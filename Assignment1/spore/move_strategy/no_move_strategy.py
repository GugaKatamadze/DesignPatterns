from spore.evolution.evolution import Evolution
from spore.move.move_result import MoveResult


class NoMoveStrategy:
    def move(self, stamina: int, evolutions: dict[Evolution, int]) -> MoveResult:
        return MoveResult()
