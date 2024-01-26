from spore.constants import CRAWL_SPEED, CRAWL_STAMINA_USAGE, STAMINA_REQUIRED_TO_CRAWL
from spore.evolution.evolution import Evolution
from spore.move.move_result import MoveResult


class Crawl:
    def move(
        self, evolution: Evolution, evolution_level: int, stamina: int
    ) -> MoveResult:
        if stamina >= STAMINA_REQUIRED_TO_CRAWL:
            return MoveResult(CRAWL_STAMINA_USAGE, CRAWL_SPEED)

        return MoveResult(0, 0)
