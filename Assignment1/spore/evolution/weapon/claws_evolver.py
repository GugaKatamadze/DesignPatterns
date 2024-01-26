from enum import Enum
from typing import Protocol

from spore.constants import (
    BIG_CLAWS_DAMAGE_MULTIPLIER,
    MEDIUM_CLAWS_DAMAGE_MULTIPLIER,
    SMALL_CLAWS_DAMAGE_MULTIPLIER,
)


class ClawsLevel(Enum):
    NONE = 0
    SMALL = SMALL_CLAWS_DAMAGE_MULTIPLIER
    MEDIUM = MEDIUM_CLAWS_DAMAGE_MULTIPLIER
    BIG = BIG_CLAWS_DAMAGE_MULTIPLIER


class ClawsEvolver(Protocol):
    def evolve(self, claws_level: ClawsLevel) -> ClawsLevel:
        pass


class NoneClawsEvolver:
    def __init__(self, next_evolver: ClawsEvolver):
        self.next_evolver = next_evolver

    def evolve(self, claws_level: ClawsLevel) -> ClawsLevel:
        if claws_level is ClawsLevel.NONE:
            return ClawsLevel.SMALL

        return self.next_evolver.evolve(claws_level)


class SmallClawsEvolver:
    def __init__(self, next_evolver: ClawsEvolver):
        self.next_evolver = next_evolver

    def evolve(self, claws_level: ClawsLevel) -> ClawsLevel:
        if claws_level is ClawsLevel.SMALL:
            return ClawsLevel.MEDIUM

        return self.next_evolver.evolve(claws_level)


class MediumClawsEvolver:
    def __init__(self, next_evolver: ClawsEvolver):
        self.next_evolver = next_evolver

    def evolve(self, claws_level: ClawsLevel) -> ClawsLevel:
        if claws_level is ClawsLevel.MEDIUM:
            return ClawsLevel.BIG

        return self.next_evolver.evolve(claws_level)


class BigClawsEvolver:
    def __init__(self, next_evolver: ClawsEvolver):
        self.next_evolver = next_evolver

    def evolve(self, claws_level: ClawsLevel) -> ClawsLevel:
        if claws_level is ClawsLevel.BIG:
            return ClawsLevel.BIG

        return self.next_evolver.evolve(claws_level)


class NoEvolver:
    def evolve(self, claws_level: ClawsLevel) -> ClawsLevel:
        return claws_level
