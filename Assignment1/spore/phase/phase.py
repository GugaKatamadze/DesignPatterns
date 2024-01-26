from typing import Protocol

from spore.creature.creature import Creature


class Phase(Protocol):
    def handle_event(self, predator: Creature, prey: Creature) -> None:
        pass
