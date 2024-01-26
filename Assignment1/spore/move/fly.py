from spore.constants import (
    FLY_SPEED,
    FLY_STAMINA_USAGE,
    STAMINA_REQUIRED_TO_FLY,
    WING_AMOUNT_REQUIRED_TO_FLY,
)
from spore.evolution.evolution import Evolution
from spore.move.crawl import Crawl
from spore.move.move import Move
from spore.move.move_result import MoveResult


class Fly:
    def __init__(self, next_move: Move = Crawl()):
        self.next_move = next_move

    def move(
        self, evolution: Evolution, evolution_level: int, stamina: int
    ) -> MoveResult:
        if (
            evolution is Evolution.WING
            and evolution_level >= WING_AMOUNT_REQUIRED_TO_FLY
            and stamina >= STAMINA_REQUIRED_TO_FLY
        ):
            return MoveResult(FLY_STAMINA_USAGE, FLY_SPEED)

        return self.next_move.move(evolution, evolution_level, stamina)
