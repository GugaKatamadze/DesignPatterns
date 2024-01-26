from typing import Protocol

from spore.evolution.evolution import Evolution


class EvolutionStrategy(Protocol):
    def get_evolutions(self, evolution_amount: int) -> list[Evolution]:
        pass
