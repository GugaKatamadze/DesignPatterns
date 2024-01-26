from spore.constants import (
    LEG_AMOUNT_REQUIRED_TO_WALK,
    STAMINA_REQUIRED_TO_WALK,
    WALK_SPEED,
    WALK_STAMINA_USAGE,
)
from spore.evolution.evolution import Evolution
from spore.move.crawl import Crawl
from spore.move.move import Move
from spore.move.move_result import MoveResult


class Walk:
    def __init__(self, next_move: Move = Crawl()):
        self.next_move = next_move

    def move(
        self, evolution: Evolution, evolution_level: int, stamina: int
    ) -> MoveResult:
        if (
            evolution is Evolution.LEG
            and evolution_level >= LEG_AMOUNT_REQUIRED_TO_WALK
            and stamina >= STAMINA_REQUIRED_TO_WALK
        ):
            return MoveResult(WALK_STAMINA_USAGE, WALK_SPEED)

        return self.next_move.move(evolution, evolution_level, stamina)
