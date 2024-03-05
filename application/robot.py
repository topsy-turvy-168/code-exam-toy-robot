from dataclasses import dataclass
from typing import Optional

from toy_robot.application.exception import RobotHasNotBeenPlacedError
from toy_robot.application.position import Position


@dataclass
class Robot:
    position: Optional[Position]

    def __init__(self):
        self.position = None

    def how_to_place(self) -> bool:
        return self.position is not None

    def left_side(self) -> None:
        if not self.how_to_place():
            raise RobotHasNotBeenPlacedError

        self.position.facing = self.position.facing.go_left()

    def right_side(self) -> None:
        if not self.how_to_place():
            raise RobotHasNotBeenPlacedError

        self.position.facing = self.position.facing.go_right()

    def report(self) -> str:
        if not self.how_to_place():
            raise RobotHasNotBeenPlacedError

        return repr(self.position)
