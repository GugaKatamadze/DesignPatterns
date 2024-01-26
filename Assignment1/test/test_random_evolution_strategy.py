from spore.evolution.evolution import Evolution
from spore.evolution_strategy.random_evolution_strategy import RandomEvolutionStrategy


def test_random_evolution_strategy() -> None:
    evolutions = [Evolution.LEG, Evolution.WING, Evolution.CLAWS, Evolution.MOUTH]

    random_evolution_strategy = RandomEvolutionStrategy(evolutions)

    for evolution in random_evolution_strategy.get_evolutions(10):
        assert evolution in evolutions
