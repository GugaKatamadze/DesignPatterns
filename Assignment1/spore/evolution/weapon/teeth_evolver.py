from enum import Enum
from typing import Protocol

from spore.constants import (
    SHARP_TEETH_ADDED_DAMAGE,
    SHARPER_TEETH_ADDED_DAMAGE,
    SHARPEST_TEETH_ADDED_DAMAGE,
)


class TeethSharpness(Enum):
    NONE = 0
    SHARP = SHARP_TEETH_ADDED_DAMAGE
    SHARPER = SHARPER_TEETH_ADDED_DAMAGE
    SHARPEST = SHARPEST_TEETH_ADDED_DAMAGE


class TeethEvolver(Protocol):
    def evolve(self, teeth_sharpness: TeethSharpness) -> TeethSharpness:
        pass


class NoneTeethEvolver:
    def __init__(self, next_evolver: TeethEvolver):
        self.next_evolver = next_evolver

    def evolve(self, teeth_sharpness: TeethSharpness) -> TeethSharpness:
        if teeth_sharpness is TeethSharpness.NONE:
            return TeethSharpness.SHARP

        return self.next_evolver.evolve(teeth_sharpness)


class SharpTeethEvolver:
    def __init__(self, next_evolver: TeethEvolver):
        self.next_evolver = next_evolver

    def evolve(self, teeth_sharpness: TeethSharpness) -> TeethSharpness:
        if teeth_sharpness is TeethSharpness.SHARP:
            return TeethSharpness.SHARPER

        return self.next_evolver.evolve(teeth_sharpness)


class SharperTeethEvolver:
    def __init__(self, next_evolver: TeethEvolver):
        self.next_evolver = next_evolver

    def evolve(self, teeth_sharpness: TeethSharpness) -> TeethSharpness:
        if teeth_sharpness is TeethSharpness.SHARPER:
            return TeethSharpness.SHARPEST

        return self.next_evolver.evolve(teeth_sharpness)


class SharpestTeethEvolver:
    def __init__(self, next_evolver: TeethEvolver):
        self.next_evolver = next_evolver

    def evolve(self, teeth_sharpness: TeethSharpness) -> TeethSharpness:
        if teeth_sharpness is TeethSharpness.SHARPEST:
            return TeethSharpness.SHARPEST

        return self.next_evolver.evolve(teeth_sharpness)


class NoEvolver:
    def evolve(self, teeth_sharpness: TeethSharpness) -> TeethSharpness:
        return teeth_sharpness
