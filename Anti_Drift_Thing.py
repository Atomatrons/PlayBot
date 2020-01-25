#!/usr/bin/env micropython
import Robot
import My_block

def Anti_Drift_Thing():
    """
    Checks is gyro is drifting, if it is, do a manual reset
    """
    print("Checking Gyro...")

    old_angle = Robot.gyro.angle
    Robot.sleep(5)
    new_angle = Robot.gyro.angle

    while old_angle != new_angle:
        old_angle = Robot.gyro.angle
        Robot.sleep(2)
        new_angle = Robot.gyro.angle
        if old_angle == new_angle:
            print("Gyro is not drifting")
            Robot.sleep(1)
            break
        else:
         print("Gyro is drifting")
        Robot.sleep(3)
    print("Gyro is not drifting")
    Robot.sleep(1)
