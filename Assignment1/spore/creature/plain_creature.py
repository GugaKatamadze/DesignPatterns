from spore.evolution.evolution import Evolution
from spore.move.move_result import MoveResult
from spore.move_strategy.move_strategy import MoveStrategy
from spore.move_strategy.no_move_strategy import NoMoveStrategy


class PlainCreature:
    def __init__(
        self,
        location: int,
        health: int,
        stamina: int,
        base_attack_power: int,
        name: str,
        move_strategy: MoveStrategy = NoMoveStrategy(),
    ):
        self.location = location
        self.health = health
        self.stamina = stamina
        self.attack_power = base_attack_power
        self.name = name
        self.move_strategy = move_strategy

        self.evolutions: dict[Evolution, int] = dict()

    def evolve(self, evolution: Evolution) -> None:
        pass

    def move(self) -> None:
        move_result: MoveResult = self.move_strategy.move(self.stamina, self.evolutions)

        self.stamina -= move_result.stamina_usage
        self.location += move_result.speed

    def get_attacked(self, health_loss: int) -> None:
        self.health -= health_loss

    def update_evolutions(self, evolution: Evolution) -> None:
        if evolution not in self.evolutions:
            self.evolutions[evolution] = 0

        self.evolutions[evolution] += 1

    def print_evolution_info(self) -> None:
        print(f"- {self.name} characteristics -")
        print(f"Health: {self.health}")
        print(f"Stamina: {self.stamina}")
        print(f"Location: {self.location}")

    def get_location(self) -> int:
        return self.location

    def get_stamina(self) -> int:
        return self.stamina

    def get_health(self) -> int:
        return self.health

    def get_attack_power(self) -> int:
        return self.attack_power

    def get_name(self) -> str:
        return self.name
