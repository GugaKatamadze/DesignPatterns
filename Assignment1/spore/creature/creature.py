from __future__ import annotations

from typing import Protocol

from spore.evolution.evolution import Evolution


class Creature(Protocol):
    def evolve(self, evolution: Evolution) -> None:
        pass

    def move(self) -> None:
        pass

    def get_attack_power(self) -> int:
        pass

    def get_attacked(self, health_loss: int) -> None:
        pass

    def update_evolutions(self, evolution: Evolution) -> None:
        pass

    def print_evolution_info(self) -> None:
        pass

    def get_location(self) -> int:
        pass

    def get_stamina(self) -> int:
        pass

    def get_health(self) -> int:
        pass

    def get_name(self) -> str:
        pass
