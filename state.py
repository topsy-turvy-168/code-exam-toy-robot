from toy_robot.application.robot import Robot
from toy_robot.application.table import Table


class State:
    def __init__(self):
        self.table = Table(5, 5)
        self.robot = Robot()
