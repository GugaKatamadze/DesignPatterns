import random

from spore.constants import (
    PREDATOR_BASE_ATTACK_POWER,
    PREDATOR_HEALTH_LOWER_BOUND,
    PREDATOR_HEALTH_UPPER_BOUND,
    PREDATOR_LOCATION_LOWER_BOUND,
    PREDATOR_LOCATION_UPPER_BOUND,
    PREDATOR_NAME,
    PREDATOR_STAMINA_LOWER_BOUND,
    PREDATOR_STAMINA_UPPER_BOUND,
    PREY_BASE_ATTACK_POWER,
    PREY_HEALTH_LOWER_BOUND,
    PREY_HEALTH_UPPER_BOUND,
    PREY_LOCATION_LOWER_BOUND,
    PREY_LOCATION_UPPER_BOUND,
    PREY_NAME,
    PREY_STAMINA_LOWER_BOUND,
    PREY_STAMINA_UPPER_BOUND,
    SIMULATION_AMOUNT,
)
from spore.creature.creature import Creature
from spore.creature.plain_creature import PlainCreature
from spore.evolution.evolution import Evolution
from spore.evolution.limb.leg import Leg
from spore.evolution.limb.wing import Wing
from spore.evolution.weapon.claws import Claws
from spore.evolution.weapon.mouth import Mouth
from spore.evolution_strategy.random_evolution_strategy import RandomEvolutionStrategy
from spore.move_strategy.naive_move_strategy import NaiveMoveStrategy
from spore.phase.chase_phase import ChasePhase
from spore.phase.evolution_phase import EvolutionPhase
from spore.phase.fight_phase import FightPhase


def create_predator() -> Creature:
    predator_location: int = random.randint(
        PREDATOR_LOCATION_LOWER_BOUND, PREDATOR_LOCATION_UPPER_BOUND
    )
    predator_health = random.randint(
        PREDATOR_HEALTH_LOWER_BOUND, PREDATOR_HEALTH_UPPER_BOUND
    )
    predator_stamina: int = random.randint(
        PREDATOR_STAMINA_LOWER_BOUND, PREDATOR_STAMINA_UPPER_BOUND
    )
    predator_base_attack_power = PREDATOR_BASE_ATTACK_POWER
    predator_name: str = PREDATOR_NAME
    predator_move_strategy = NaiveMoveStrategy()

    plain_predator = PlainCreature(
        predator_location,
        predator_health,
        predator_stamina,
        predator_base_attack_power,
        predator_name,
        predator_move_strategy,
    )

    decorated_predator = Claws(Mouth(Wing(Leg(plain_predator))))

    return decorated_predator


def create_prey() -> Creature:
    prey_location: int = random.randint(
        PREY_LOCATION_LOWER_BOUND, PREY_LOCATION_UPPER_BOUND
    )
    prey_health = random.randint(PREY_HEALTH_LOWER_BOUND, PREY_HEALTH_UPPER_BOUND)
    prey_stamina: int = random.randint(
        PREY_STAMINA_LOWER_BOUND, PREY_STAMINA_UPPER_BOUND
    )
    prey_base_attack_power = PREY_BASE_ATTACK_POWER
    prey_name: str = PREY_NAME
    prey_move_strategy = NaiveMoveStrategy()

    plain_prey = PlainCreature(
        prey_location,
        prey_health,
        prey_stamina,
        prey_base_attack_power,
        prey_name,
        prey_move_strategy,
    )

    decorated_prey = Claws(Mouth(Wing(Leg(plain_prey))))

    return decorated_prey


def simulate() -> None:
    simulation_amount = SIMULATION_AMOUNT
    current_simulation_number = 1

    evolutions = [Evolution.LEG, Evolution.WING, Evolution.CLAWS, Evolution.MOUTH]

    chain_of_phases = EvolutionPhase(
        RandomEvolutionStrategy(evolutions), ChasePhase(FightPhase())
    )

    while current_simulation_number <= simulation_amount:
        print(f"--- Simulation {current_simulation_number} ---")

        chain_of_phases.handle_event(create_predator(), create_prey())

        print(f"--- End of simulation {current_simulation_number} ---\n")

        current_simulation_number += 1


if __name__ == "__main__":
    simulate()
