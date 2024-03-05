from typing import Optional

from toy_robot.application.position import Direction
from toy_robot.state import State

_STATE: Optional[State] = None


def start_session() -> None:
    global _STATE
    if not _STATE:
        _STATE = State()


def turn_left() -> None:
    _STATE.robot.turn_left()


def turn_right() -> None:
    _STATE.robot.turn_right()


def move() -> None:
    _STATE.table.move_forward(_STATE.robot)


def place(x: int, y: int, facing: Direction) -> None:
    _STATE.table.place(_STATE.robot, x, y, facing)


def report() -> str:
    return _STATE.robot.report()
