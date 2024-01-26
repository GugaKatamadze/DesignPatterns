from spore.constants import (
    HOP_SPEED,
    HOP_STAMINA_USAGE,
    LEG_AMOUNT_REQUIRED_TO_HOP,
    STAMINA_REQUIRED_TO_HOP,
)
from spore.evolution.evolution import Evolution
from spore.move.crawl import Crawl
from spore.move.move import Move
from spore.move.move_result import MoveResult


class Hop:
    def __init__(self, next_move: Move = Crawl()):
        self.next_move = next_move

    def move(
        self, evolution: Evolution, evolution_level: int, stamina: int
    ) -> MoveResult:
        if (
            evolution is Evolution.LEG
            and evolution_level >= LEG_AMOUNT_REQUIRED_TO_HOP
            and stamina >= STAMINA_REQUIRED_TO_HOP
        ):
            return MoveResult(HOP_STAMINA_USAGE, HOP_SPEED)

        return self.next_move.move(evolution, evolution_level, stamina)
