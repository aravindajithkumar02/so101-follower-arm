# D:\sweep_arm.py
import time
from lerobot.robots.so_follower import SOFollower, SOFollowerRobotConfig

robot = SOFollower(SOFollowerRobotConfig(port='COM5'))
robot.connect()

joints = ['shoulder_pan', 'shoulder_lift', 'elbow_flex', 'wrist_flex', 'wrist_roll', 'gripper']

for joint in joints:
    angle = -30.0 if joint == 'elbow_flex' else 30.0
    print(f"Moving {joint} to {angle}°...")
    action = {f'{j}.pos': 0.0 for j in joints}
    action[f'{joint}.pos'] = angle
    robot.send_action(action)
    time.sleep(2)
    action = {f'{j}.pos': 0.0 for j in joints}
    robot.send_action(action)
    time.sleep(1.5)

print("Sweep done")
robot.disconnect()