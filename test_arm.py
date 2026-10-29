import time
from lerobot.robots.so_follower import SOFollower, SOFollowerRobotConfig
robot = SOFollower(SOFollowerRobotConfig(port='COM5'))
robot.connect()
print(robot.get_observation())
time.sleep(2)
robot.disconnect()