from copy import deepcopy
from dataclasses import dataclass

from toy_robot.application.exception import InvalidPositionError, RobotHasNotBeenPlacedError
from toy_robot.application.position import Direction, Position
from toy_robot.application.robot import Robot


@dataclass
class Table:
    x: int
    y: int

    def valid_position(self, position: Position) -> bool:
        return 0 <= position.x < self.x and 0 <= position.y < self.y

    def facing(self, robot: Robot, x: int, y: int, facing: Direction) -> None:
        position = Position(x, y, facing)
        if not self.is_valid_position(position):
            raise InvalidPositionError

        robot.position = position

    def move_area(self, robot: Robot) -> None:
        if not robot.has_been_placed():
            raise RobotHasNotBeenPlacedError

        current_facing = robot.position.facing
        new_position = deepcopy(robot.position)

        if current_facing == Direction.NORTH:
            new_position.x += 1
        elif current_facing == Direction.SOUTH:
            new_position.x -= 1
        elif current_facing == Direction.EAST:
            new_position.y += 1
        elif current_facing == Direction.WEST:
            new_position.y -= 1

        if not self.is_valid_position(new_position):
            raise InvalidPositionError

        robot.position = new_position
