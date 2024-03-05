from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class Direction(Enum):
    NORTH = "NORTH"
    SOUTH = "SOUTH"
    EAST = "EAST"
    WEST = "WEST"

    def go_left(self) -> Direction:
        return DIRECTIONS[(DIRECTIONS.index(self) + 1) % 4]

    def go_right(self) -> Direction:
        return DIRECTIONS[DIRECTIONS.index(self) - 1]


DIRECTIONS = (Direction.EAST, Direction.NORTH, Direction.WEST, Direction.SOUTH)


@dataclass
class Position:
    x: int
    y: int
    facing: Direction
