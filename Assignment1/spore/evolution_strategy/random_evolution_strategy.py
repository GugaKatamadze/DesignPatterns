import random

from spore.evolution.evolution import Evolution


class RandomEvolutionStrategy:
    def __init__(self, evolutions: list[Evolution]):
        self.evolutions = evolutions

    def get_evolutions(self, evolution_amount: int) -> list[Evolution]:
        evolutions = []

        for _ in range(evolution_amount):
            evolutions.append(self.get_next_evolution())

        return evolutions

    def get_next_evolution(self) -> Evolution:
        random_index = random.randint(0, len(self.evolutions) - 1)

        return self.evolutions[random_index]
