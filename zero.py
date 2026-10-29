# D:\hold_zero.py
import time
from lerobot.robots.so_follower import SOFollower, SOFollowerRobotConfig

robot = SOFollower(SOFollowerRobotConfig(port='COM5'))
robot.connect()

joints = ['shoulder_pan', 'shoulder_lift', 'elbow_flex', 'wrist_flex', 'wrist_roll', 'gripper']
zero = {f'{j}.pos': 0.0 for j in joints}

# Smooth move to zero
current = robot.get_observation()
steps = 30
for i in range(1, steps + 1):
    action = {}
    for j in joints:
        start = current[f'{j}.pos']
        action[f'{j}.pos'] = start + (0.0 - start) * (i / steps)
    robot.send_action(action)
    time.sleep(0.05)

print("At zero. Holding. Press Ctrl+C to stop.")
try:
    while True:
        robot.send_action(zero)
        time.sleep(0.5)
except KeyboardInterrupt:
    pass

robot.disconnect()