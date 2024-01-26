from spore.constants import (
    LEG_AMOUNT_REQUIRED_TO_RUN,
    RUN_SPEED,
    RUN_STAMINA_USAGE,
    STAMINA_REQUIRED_TO_RUN,
)
from spore.evolution.evolution import Evolution
from spore.move.crawl import Crawl
from spore.move.move import Move
from spore.move.move_result import MoveResult


class Run:
    def __init__(self, next_move: Move = Crawl()):
        self.next_move = next_move

    def move(
        self, evolution: Evolution, evolution_level: int, stamina: int
    ) -> MoveResult:
        if (
            evolution is Evolution.LEG
            and evolution_level >= LEG_AMOUNT_REQUIRED_TO_RUN
            and stamina >= STAMINA_REQUIRED_TO_RUN
        ):
            return MoveResult(RUN_STAMINA_USAGE, RUN_SPEED)

        return self.next_move.move(evolution, evolution_level, stamina)
