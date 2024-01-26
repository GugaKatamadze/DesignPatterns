from spore.constants import PREDATOR_EVOLUTION_AMOUNT, PREY_EVOLUTION_AMOUNT
from spore.creature.creature import Creature
from spore.evolution_strategy.evolution_strategy import EvolutionStrategy
from spore.phase.end_phase import EndPhase
from spore.phase.phase import Phase


class EvolutionPhase:
    def __init__(
        self, evolution_strategy: EvolutionStrategy, next_phase: Phase = EndPhase()
    ):
        self.evolution_strategy = evolution_strategy
        self.next_phase = next_phase

        self.predator_evolution_amount = PREDATOR_EVOLUTION_AMOUNT
        self.prey_evolution_amount = PREY_EVOLUTION_AMOUNT

    def handle_event(self, predator: Creature, prey: Creature) -> None:
        self.evolve_creature(predator, self.predator_evolution_amount)
        self.evolve_creature(prey, self.prey_evolution_amount)

        predator.print_evolution_info()
        prey.print_evolution_info()

        self.next_phase.handle_event(predator, prey)

    def evolve_creature(self, creature: Creature, evolution_amount: int) -> None:
        for evolution in self.evolution_strategy.get_evolutions(evolution_amount):
            creature.evolve(evolution)
