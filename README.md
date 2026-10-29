# SO-101 Follower Arm

6-DOF robotic arm built from the SO-101 follower kit. This is a portfolio project — I'm learning robotics hands-on while applying for jobs in Germany.

The arm runs on Feetech STS3215 servos controlled through the LeRobot framework. Everything here is what I actually got working, including the bugs I had to fix along the way.

---

## Hardware

- SO-101 follower kit (3D printed frame, PETG)
- 6x Feetech STS3215 servo (4096 ticks/rev)
- Waveshare Serial Bus Servo Driver Board
- USB connection on COM5 (Windows)

Motor IDs, base to gripper: shoulder_pan=1, shoulder_lift=2, elbow_flex=3, wrist_flex=4, wrist_roll=5, gripper=6

Board is wired at the base end — learned the hard way that putting it at the gripper end means the cable moves with the arm.

---

## Software

- Python 3.12
- LeRobot v0.6.2 (Hugging Face)
- Windows 11

---

## Scripts

**`test_arm.py`** — prints current joint positions. Useful for debugging and checking calibration.

**`hold_zero.py`** — moves to calibration zero and holds. The loop is necessary because STS3215 servos go limp the moment the connection drops — without it the arm just falls.

**`home.py`** — same as hold_zero but with wrist_flex at 70.5° so the gripper points downward. This is the actual resting pose I use.

**`sweep_arm.py`** — moves each joint 30° and back in sequence. Good for a quick demo.

Run with:
```
py -3.12 scripts\<filename>.py
```

Press `Ctrl+C` to stop any script.

---

## Calibration

LeRobot stores calibration at:
```
~\.cache\huggingface\lerobot\calibration\robots\so_follower\None.json
```
To recalibrate:
```
py -3.12 -m lerobot.calibrate --robot-path lerobot/configs/robot/so_follower.yaml
```

Put the arm in the position you want as zero before hitting Enter on the "middle position" step. Don't edit `homing_offset` in the JSON directly unless you know what you're doing — I tried, the motor strained against the hard stop.

The resting pose has `wrist_flex` at 70.5° rather than 0°. I set this in code instead of touching the calibration file.

---

## Things I ran into

- Loose connector between servo 2 and 3 caused a motor timeout during calibration — reseating it fixed it
- `wrist_flex` physically maxes out around 2300 ticks instead of the expected ~3200 — mechanical limit of the printed parts, not a software issue
- Windows CMD doesn't support multiline `-c` strings, save everything as a `.py` file
- Arm collapses on disconnect — keep-alive loop in every script that holds a position

---

## TODO

- [ ] Demo video
- [ ] Wiring diagram
- [ ] ROS 2 integration
- [ ] Teleoperation with leader arm