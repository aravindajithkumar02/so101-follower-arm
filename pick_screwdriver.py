import time
from lerobot.robots.so_follower import SOFollower, SOFollowerRobotConfig

robot = SOFollower(SOFollowerRobotConfig(port='COM5'))
robot.connect()

def interpolate(robot, start, end, steps=40, step_delay=0.05):
    for i in range(1, steps + 1):
        action = {}
        for key in end:
            action[key] = start[key] + (end[key] - start[key]) * (i / steps)
        robot.send_action(action)
        time.sleep(step_delay)

def get_pos(robot):
    obs = robot.get_observation()
    return {k.replace('.pos', '') + '.pos': v for k, v in obs.items()}

home = {
    'shoulder_pan.pos': 0.0,
    'shoulder_lift.pos': 0.0,
    'elbow_flex.pos': 0.0,
    'wrist_flex.pos': 70.5,
    'wrist_roll.pos': 0.0,
    'gripper.pos': 0.0,
}

hover = {
    'shoulder_pan.pos': -0.31,
    'shoulder_lift.pos': 142.59,
    'elbow_flex.pos': -145.27,
    'wrist_flex.pos': 98.33,
    'wrist_roll.pos': 0.13,
    'gripper.pos': 30.0,
}

pick = {
    'shoulder_pan.pos': -1.98,
    'shoulder_lift.pos': 154.11,
    'elbow_flex.pos': -141.05,
    'wrist_flex.pos': 93.05,
    'wrist_roll.pos': 0.13,
    'gripper.pos': 30.0,
}

pick_closed = dict(pick)
pick_closed['gripper.pos'] = 0.0

lift = {
    'shoulder_pan.pos': -3.47,
    'shoulder_lift.pos': 124.84,
    'elbow_flex.pos': -140.70,
    'wrist_flex.pos': 101.85,
    'wrist_roll.pos': 0.22,
    'gripper.pos': 0.0,
}

try:
    print("Moving to home...")
    current = get_pos(robot)
    interpolate(robot, current, home, steps=80)
    time.sleep(1.0)

    print("Moving to hover above screwdriver...")
    interpolate(robot, home, hover, steps=60)
    time.sleep(0.50)

    print("Lowering to screwdriver...")
    interpolate(robot, hover, pick, steps=30)
    time.sleep(0.5)

    print("Closing gripper...")
    interpolate(robot, pick, pick_closed, steps=20)
    time.sleep(0.5)

    print("Lifting with screwdriver...")
    interpolate(robot, pick_closed, lift, steps=50)
    time.sleep(1.0)

    print("Returning home with screwdriver...")
    interpolate(robot, lift, home, steps=80)
    time.sleep(1.0)

    print("Releasing at home...")
    home_open = dict(home)
    home_open['gripper.pos'] = 30.0
    interpolate(robot, home, home_open, steps=20)
    
    print("Closing gripper...")
    interpolate(robot, home_open, home, steps=20) 	

except KeyboardInterrupt:
    print("Interrupted. Returning home...")
    current = get_pos(robot)
    home_gripping = dict(home)
    home_gripping['gripper.pos'] = 0.0
    interpolate(robot, current, home_gripping, steps=80)
    time.sleep(0.50)
    home_open = dict(home)
    home_open['gripper.pos'] = 30.0
    interpolate(robot, home_gripping, home_open, steps=20)

robot.disconnect()