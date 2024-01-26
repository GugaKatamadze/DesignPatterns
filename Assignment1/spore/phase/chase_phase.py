from spore.creature.creature import Creature
from spore.phase.end_phase import EndPhase
from spore.phase.phase import Phase


class ChasePhase:
    def __init__(self, next_phase: Phase = EndPhase()):
        self.next_phase = next_phase

    def handle_event(self, predator: Creature, prey: Creature) -> None:
        while predator.get_stamina() > 0:
            prey.move()
            predator.move()

            if predator.get_location() >= prey.get_location():
                self.next_phase.handle_event(predator, prey)

                return

        print("Prey ran into infinity")
