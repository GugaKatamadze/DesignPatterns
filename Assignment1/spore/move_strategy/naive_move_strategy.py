from spore.constants import CRAWL_SPEED, CRAWL_STAMINA_USAGE, STAMINA_REQUIRED_TO_CRAWL
from spore.evolution.evolution import Evolution
from spore.move.fly import Fly
from spore.move.hop import Hop
from spore.move.move_result import MoveResult
from spore.move.run import Run
from spore.move.walk import Walk


class NaiveMoveStrategy:
    def move(self, stamina: int, evolutions: dict[Evolution, int]) -> MoveResult:
        if stamina < STAMINA_REQUIRED_TO_CRAWL:
            return MoveResult(0, 0)

        move_chain = Fly(Run(Walk(Hop())))

        move_result = MoveResult(CRAWL_STAMINA_USAGE, CRAWL_SPEED)

        for evolution, evolution_level in evolutions.items():
            current_move_result = move_chain.move(evolution, evolution_level, stamina)

            if current_move_result.speed > move_result.speed:
                move_result = current_move_result

        return move_result
