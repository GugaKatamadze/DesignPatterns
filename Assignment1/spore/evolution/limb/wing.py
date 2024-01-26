from spore.creature.creature import Creature
from spore.creature.creature_decorator import CreatureDecorator
from spore.evolution.evolution import Evolution


class Wing(CreatureDecorator):
    def __init__(self, creature: Creature):
        super().__init__(creature)

        self.evolution_level = 0

    def evolve(self, evolution: Evolution) -> None:
        if evolution is Evolution.WING:
            self.evolution_level += 1

            super().update_evolutions(evolution)
        else:
            super().evolve(evolution)

    def print_evolution_info(self) -> None:
        super().print_evolution_info()

        if self.evolution_level > 0:
            print(f"Wings: {self.evolution_level}")
