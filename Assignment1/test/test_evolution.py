from spore.constants import (
    BIG_CLAWS_DAMAGE_MULTIPLIER,
    MEDIUM_CLAWS_DAMAGE_MULTIPLIER,
    SHARP_TEETH_ADDED_DAMAGE,
    SHARPER_TEETH_ADDED_DAMAGE,
    SHARPEST_TEETH_ADDED_DAMAGE,
    SMALL_CLAWS_DAMAGE_MULTIPLIER,
)
from spore.creature.plain_creature import PlainCreature
from spore.evolution.evolution import Evolution
from spore.evolution.limb.leg import Leg
from spore.evolution.limb.wing import Wing
from spore.evolution.weapon.claws import Claws
from spore.evolution.weapon.claws_evolver import ClawsLevel
from spore.evolution.weapon.mouth import Mouth
from spore.evolution.weapon.teeth_evolver import TeethSharpness


def test_evolve_leg() -> None:
    creature_with_leg = Leg(
        PlainCreature(
            0,
            0,
            0,
            1,
            "",
        )
    )

    creature_with_leg.evolve(Evolution.LEG)

    assert creature_with_leg.evolution_level == 1


def test_evolve_wing() -> None:
    creature_with_wing = Wing(PlainCreature(0, 0, 0, 1, ""))

    creature_with_wing.evolve(Evolution.WING)

    assert creature_with_wing.evolution_level == 1


def test_evolve_none_claws() -> None:
    creature_with_claws = Claws(PlainCreature(0, 0, 0, 2, ""))

    creature_with_claws.evolve(Evolution.CLAWS)

    assert creature_with_claws.evolution_level == ClawsLevel.SMALL
    assert creature_with_claws.get_attack_power() == 2 * SMALL_CLAWS_DAMAGE_MULTIPLIER


def test_evolve_small_claws() -> None:
    creature_with_claws = Claws(PlainCreature(0, 0, 0, 2, ""))

    creature_with_claws.evolve(Evolution.CLAWS)
    creature_with_claws.evolve(Evolution.CLAWS)

    assert creature_with_claws.evolution_level == ClawsLevel.MEDIUM
    assert creature_with_claws.get_attack_power() == 2 * MEDIUM_CLAWS_DAMAGE_MULTIPLIER


def test_evolve_medium_claws() -> None:
    creature_with_claws = Claws(PlainCreature(0, 0, 0, 2, ""))

    creature_with_claws.evolve(Evolution.CLAWS)
    creature_with_claws.evolve(Evolution.CLAWS)
    creature_with_claws.evolve(Evolution.CLAWS)

    assert creature_with_claws.evolution_level == ClawsLevel.BIG
    assert creature_with_claws.get_attack_power() == 2 * BIG_CLAWS_DAMAGE_MULTIPLIER


def test_evolve_big_claws() -> None:
    creature_with_claws = Claws(PlainCreature(0, 0, 0, 2, ""))

    creature_with_claws.evolve(Evolution.CLAWS)
    creature_with_claws.evolve(Evolution.CLAWS)
    creature_with_claws.evolve(Evolution.CLAWS)
    creature_with_claws.evolve(Evolution.CLAWS)

    assert creature_with_claws.evolution_level == ClawsLevel.BIG
    assert creature_with_claws.get_attack_power() == 2 * BIG_CLAWS_DAMAGE_MULTIPLIER


def test_evolve_none_teeth_mouth() -> None:
    creature_with_mouth = Mouth(PlainCreature(0, 0, 0, 1, ""))

    creature_with_mouth.evolve(Evolution.MOUTH)

    assert creature_with_mouth.evolution_level == TeethSharpness.SHARP
    assert creature_with_mouth.get_attack_power() == 1 + SHARP_TEETH_ADDED_DAMAGE


def test_evolve_sharp_teeth_mouth() -> None:
    creature_with_mouth = Mouth(PlainCreature(0, 0, 0, 1, ""))

    creature_with_mouth.evolve(Evolution.MOUTH)
    creature_with_mouth.evolve(Evolution.MOUTH)

    assert creature_with_mouth.evolution_level == TeethSharpness.SHARPER
    assert creature_with_mouth.get_attack_power() == 1 + SHARPER_TEETH_ADDED_DAMAGE


def test_evolve_sharper_teeth_mouth() -> None:
    creature_with_mouth = Mouth(PlainCreature(0, 0, 0, 1, ""))

    creature_with_mouth.evolve(Evolution.MOUTH)
    creature_with_mouth.evolve(Evolution.MOUTH)
    creature_with_mouth.evolve(Evolution.MOUTH)

    assert creature_with_mouth.evolution_level == TeethSharpness.SHARPEST
    assert creature_with_mouth.get_attack_power() == 1 + SHARPEST_TEETH_ADDED_DAMAGE


def test_evolve_sharpest_teeth_mouth() -> None:
    creature_with_mouth = Mouth(PlainCreature(0, 0, 0, 1, ""))

    creature_with_mouth.evolve(Evolution.MOUTH)
    creature_with_mouth.evolve(Evolution.MOUTH)
    creature_with_mouth.evolve(Evolution.MOUTH)
    creature_with_mouth.evolve(Evolution.MOUTH)

    assert creature_with_mouth.evolution_level == TeethSharpness.SHARPEST
    assert creature_with_mouth.get_attack_power() == 1 + SHARPEST_TEETH_ADDED_DAMAGE
