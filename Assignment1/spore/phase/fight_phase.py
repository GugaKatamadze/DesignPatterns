from spore.creature.creature import Creature
from spore.phase.end_phase import EndPhase
from spore.phase.phase import Phase


class FightPhase:
    def __init__(self, next_phase: Phase = EndPhase()):
        self.next_phase = next_phase

    def handle_event(self, predator: Creature, prey: Creature) -> None:
        predator_attack_power = predator.get_attack_power()
        prey_attack_power = prey.get_attack_power()

        if predator_attack_power == prey_attack_power == 0:
            print("What a show")

            return

        while True:
            if predator.get_health() > 0:
                prey.get_attacked(predator_attack_power)
            else:
                print("Prey ran into infinity")

                return

            if prey.get_health() > 0:
                predator.get_attacked(prey_attack_power)
            else:
                print("Some R-rated things have happened")

                return
