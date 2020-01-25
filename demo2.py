#!/usr/bin/env micropython
import Robot
import My_block
from sys import stderr

"""
    What does this demo do???
"""

Robot.ShivaGyro.compass_point = 0

print("robot ready", stderr)

Robot.steer_pair.off(brake = True)

while True:
    Robot.steer_pair.off(brake = True)
    front_distance = Robot.ultra.distances_inches
    rear_distance = Robot.infared.proximity
    if rear_distance is None:
        rear_distance = 1000
    if rear_distance > 6 and front_distance > 10:
        rear_distance = Robot.infared.proximity
        Robot.right_attachment.on_for_seconds(20, 2)
    Robot.steer_pair.off(brake = True)
    if rear_distance < 6:
       Robot.steer_pair.on_for_rotations(0, 80, 3)
       Robot.right_attachment.on_for_seconds(80, 4)
    Robot,steer_pair.off(brake = True)
    if front_distance < 10:
        Robot.steer_pair.on_for_seconds(0,-80, 3)
        Robot.right_attachment.on_for_seconds(-80, 4)
    Robot.steer_pair.off(brake = True)
