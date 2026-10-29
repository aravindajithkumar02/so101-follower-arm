import time
from lerobot.robots.so_follower import SOFollower, SOFollowerRobotConfig
robot = SOFollower(SOFollowerRobotConfig(port='COM5'))
robot.connect()
print("Current position:", robot.get_observation())
action = {
    'shoulder_pan.pos': 45.0,
    'shoulder_lift.pos': 0.0,
    'elbow_flex.pos': 0.0,
    'wrist_flex.pos': 0.0,
    'wrist_roll.pos': 0.0,
    'gripper.pos': 0.0,
}
print("Moving shoulder pan 45 degrees...")
robot.send_action(action)
time.sleep(3)
print("Done")
robot.disconnect()