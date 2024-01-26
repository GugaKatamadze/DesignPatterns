from spore.constants import (
    CRAWL_SPEED,
    CRAWL_STAMINA_USAGE,
    FLY_SPEED,
    FLY_STAMINA_USAGE,
    HOP_SPEED,
    HOP_STAMINA_USAGE,
    LEG_AMOUNT_REQUIRED_TO_HOP,
    LEG_AMOUNT_REQUIRED_TO_RUN,
    LEG_AMOUNT_REQUIRED_TO_WALK,
    RUN_SPEED,
    RUN_STAMINA_USAGE,
    STAMINA_REQUIRED_TO_CRAWL,
    STAMINA_REQUIRED_TO_FLY,
    STAMINA_REQUIRED_TO_HOP,
    STAMINA_REQUIRED_TO_RUN,
    STAMINA_REQUIRED_TO_WALK,
    WALK_SPEED,
    WALK_STAMINA_USAGE,
    WING_AMOUNT_REQUIRED_TO_FLY,
)
from spore.evolution.evolution import Evolution
from spore.move.crawl import Crawl
from spore.move.fly import Fly
from spore.move.hop import Hop
from spore.move.run import Run
from spore.move.walk import Walk


def test_crawl() -> None:
    crawl = Crawl()

    evolution = Evolution.LEG
    evolution_level = 0
    stamina = STAMINA_REQUIRED_TO_CRAWL

    move_result = crawl.move(evolution, evolution_level, stamina)

    assert move_result.stamina_usage == CRAWL_STAMINA_USAGE
    assert move_result.speed == CRAWL_SPEED


def test_hop() -> None:
    hop = Hop()

    evolution = Evolution.LEG
    evolution_level = LEG_AMOUNT_REQUIRED_TO_HOP
    stamina = STAMINA_REQUIRED_TO_HOP

    move_result = hop.move(evolution, evolution_level, stamina)

    assert move_result.stamina_usage == HOP_STAMINA_USAGE
    assert move_result.speed == HOP_SPEED


def test_walk() -> None:
    walk = Walk()

    evolution = Evolution.LEG
    evolution_level = LEG_AMOUNT_REQUIRED_TO_WALK
    stamina = STAMINA_REQUIRED_TO_WALK

    move_result = walk.move(evolution, evolution_level, stamina)

    assert move_result.stamina_usage == WALK_STAMINA_USAGE
    assert move_result.speed == WALK_SPEED


def test_run() -> None:
    run = Run()

    evolution = Evolution.LEG
    evolution_level = LEG_AMOUNT_REQUIRED_TO_RUN
    stamina = STAMINA_REQUIRED_TO_RUN

    move_result = run.move(evolution, evolution_level, stamina)

    assert move_result.stamina_usage == RUN_STAMINA_USAGE
    assert move_result.speed == RUN_SPEED


def test_fly() -> None:
    fly = Fly()

    evolution = Evolution.WING
    evolution_level = WING_AMOUNT_REQUIRED_TO_FLY
    stamina = STAMINA_REQUIRED_TO_FLY

    move_result = fly.move(evolution, evolution_level, stamina)

    assert move_result.stamina_usage == FLY_STAMINA_USAGE
    assert move_result.speed == FLY_SPEED
