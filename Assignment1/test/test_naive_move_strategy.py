from spore.constants import (
    CRAWL_SPEED,
    CRAWL_STAMINA_USAGE,
    FLY_SPEED,
    FLY_STAMINA_USAGE,
    HOP_SPEED,
    HOP_STAMINA_USAGE,
    LEG_AMOUNT_REQUIRED_TO_RUN,
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
from spore.move_strategy.naive_move_strategy import NaiveMoveStrategy


def test_should_crawl() -> None:
    naive_move_strategy = NaiveMoveStrategy()

    stamina = STAMINA_REQUIRED_TO_CRAWL
    evolutions = {
        Evolution.LEG: LEG_AMOUNT_REQUIRED_TO_RUN,
        Evolution.WING: WING_AMOUNT_REQUIRED_TO_FLY,
    }

    move_result = naive_move_strategy.move(stamina, evolutions)

    assert move_result.stamina_usage == CRAWL_STAMINA_USAGE
    assert move_result.speed == CRAWL_SPEED


def test_should_hop() -> None:
    naive_move_strategy = NaiveMoveStrategy()

    stamina = STAMINA_REQUIRED_TO_HOP
    evolutions = {
        Evolution.LEG: LEG_AMOUNT_REQUIRED_TO_RUN,
        Evolution.WING: WING_AMOUNT_REQUIRED_TO_FLY,
    }

    move_result = naive_move_strategy.move(stamina, evolutions)

    assert move_result.stamina_usage == HOP_STAMINA_USAGE
    assert move_result.speed == HOP_SPEED


def test_should_walk() -> None:
    naive_move_strategy = NaiveMoveStrategy()

    stamina = STAMINA_REQUIRED_TO_WALK
    evolutions = {
        Evolution.LEG: LEG_AMOUNT_REQUIRED_TO_RUN,
        Evolution.WING: WING_AMOUNT_REQUIRED_TO_FLY,
    }

    move_result = naive_move_strategy.move(stamina, evolutions)

    assert move_result.stamina_usage == WALK_STAMINA_USAGE
    assert move_result.speed == WALK_SPEED


def test_should_run() -> None:
    naive_move_strategy = NaiveMoveStrategy()

    stamina = STAMINA_REQUIRED_TO_RUN
    evolutions = {
        Evolution.LEG: LEG_AMOUNT_REQUIRED_TO_RUN,
        Evolution.WING: WING_AMOUNT_REQUIRED_TO_FLY,
    }

    move_result = naive_move_strategy.move(stamina, evolutions)

    assert move_result.stamina_usage == RUN_STAMINA_USAGE
    assert move_result.speed == RUN_SPEED


def test_should_fly() -> None:
    naive_move_strategy = NaiveMoveStrategy()

    stamina = STAMINA_REQUIRED_TO_FLY
    evolutions = {
        Evolution.LEG: LEG_AMOUNT_REQUIRED_TO_RUN,
        Evolution.WING: WING_AMOUNT_REQUIRED_TO_FLY,
    }

    move_result = naive_move_strategy.move(stamina, evolutions)

    assert move_result.stamina_usage == FLY_STAMINA_USAGE
    assert move_result.speed == FLY_SPEED
