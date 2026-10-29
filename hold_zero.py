import time
from lerobot.robots.so_follower import SOFollower, SOFollowerRobotConfig

robot = SOFollower(SOFollowerRobotConfig(port='COM5'))
robot.connect()

joints = ['shoulder_pan', 'shoulder_lift', 'elbow_flex', 'wrist_flex', 'wrist_roll', 'gripper']
pose = {
    'shoulder_pan.pos': 0.0,
    'shoulder_lift.pos': 0.0,
    'elbow_flex.pos': 0.0,
    'wrist_flex.pos': 70.5,
    'wrist_roll.pos': 0.0,
    'gripper.pos': 0.0,
}

print("Moving to rest pose. Press Ctrl+C to stop.")
robot.send_action(pose)
time.sleep(3)

try:
    while True:
        robot.send_action(pose)
        time.sleep(0.5)
except KeyboardInterrupt:
    pass

robot.disconnect()