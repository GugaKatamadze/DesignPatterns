from spore.creature.creature import Creature
from spore.evolution.evolution import Evolution


class CreatureDecorator:
    def __init__(self, creature: Creature):
        self.creature = creature

    def evolve(self, evolution: Evolution) -> None:
        self.creature.evolve(evolution)

    def move(self) -> None:
        self.creature.move()

    def get_attack_power(self) -> int:
        return self.creature.get_attack_power()

    def get_attacked(self, health_loss: int) -> None:
        self.creature.get_attacked(health_loss)

    def update_evolutions(self, evolution: Evolution) -> None:
        self.creature.update_evolutions(evolution)

    def print_evolution_info(self) -> None:
        self.creature.print_evolution_info()

    def get_location(self) -> int:
        return self.creature.get_location()

    def get_stamina(self) -> int:
        return self.creature.get_stamina()

    def get_health(self) -> int:
        return self.creature.get_health()

    def get_name(self) -> str:
        return self.creature.get_name()
