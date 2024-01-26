from spore.creature.creature import Creature
from spore.creature.creature_decorator import CreatureDecorator
from spore.evolution.evolution import Evolution
from spore.evolution.weapon.teeth_evolver import (
    NoEvolver,
    NoneTeethEvolver,
    SharperTeethEvolver,
    SharpestTeethEvolver,
    SharpTeethEvolver,
    TeethSharpness,
)


class Mouth(CreatureDecorator):
    def __init__(self, creature: Creature):
        super().__init__(creature)

        self.evolution_level = TeethSharpness.NONE
        self.evolver = NoneTeethEvolver(
            SharpTeethEvolver(SharperTeethEvolver(SharpestTeethEvolver(NoEvolver())))
        )

    def evolve(self, evolution: Evolution) -> None:
        if evolution is Evolution.MOUTH:
            self.evolution_level = self.evolver.evolve(self.evolution_level)
        else:
            super().evolve(evolution)

    def get_attack_power(self) -> int:
        return self.evolution_level.value + super().get_attack_power()

    def print_evolution_info(self) -> None:
        super().print_evolution_info()

        if self.evolution_level is not TeethSharpness.NONE:
            print(f"Teeth: {self.evolution_level.name}")
