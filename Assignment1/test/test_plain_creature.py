from spore.creature.plain_creature import PlainCreature
from spore.evolution.evolution import Evolution


def test_get_location() -> None:
    plain_creature = PlainCreature(0, 0, 0, 1, "")

    assert plain_creature.get_location() == 0


def test_get_health() -> None:
    plain_creature = PlainCreature(0, 0, 0, 1, "")

    assert plain_creature.get_health() == 0


def test_get_stamina() -> None:
    plain_creature = PlainCreature(0, 0, 0, 1, "")

    assert plain_creature.get_stamina() == 0


def test_get_name() -> None:
    plain_creature = PlainCreature(0, 0, 0, 1, "")

    assert plain_creature.get_name() == ""


def test_get_attack_power() -> None:
    plain_creature = PlainCreature(0, 0, 0, 1, "")

    assert plain_creature.get_attack_power() == 1


def test_get_attacked() -> None:
    plain_creature = PlainCreature(0, 1, 0, 1, "")

    plain_creature.get_attacked(1)

    assert plain_creature.get_health() == 0


def test_update_evolutions() -> None:
    plain_creature = PlainCreature(0, 0, 0, 1, "")

    plain_creature.update_evolutions(Evolution.LEG)
    plain_creature.update_evolutions(Evolution.WING)
    plain_creature.update_evolutions(Evolution.WING)
    plain_creature.update_evolutions(Evolution.CLAWS)
    plain_creature.update_evolutions(Evolution.CLAWS)
    plain_creature.update_evolutions(Evolution.CLAWS)
    plain_creature.update_evolutions(Evolution.MOUTH)
    plain_creature.update_evolutions(Evolution.MOUTH)
    plain_creature.update_evolutions(Evolution.MOUTH)
    plain_creature.update_evolutions(Evolution.MOUTH)

    assert plain_creature.evolutions == {
        Evolution.LEG: 1,
        Evolution.WING: 2,
        Evolution.CLAWS: 3,
        Evolution.MOUTH: 4,
    }
