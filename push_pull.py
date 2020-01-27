#!/usr/bin/env micropython
import Robot
import My_block
from sys import stderr

"""
    What does this demo do???
"""

Robot.ShivaGyro.compass_point = 0

print("robot ready", stderr)

while True:
    # get distance of user from ultrasonic
    front_distance = Robot.ultra.distance_inches
    # Robot.debug_print("front_distance: {}".format(front_distance))

    # If user is way too close, back up quickly
    # if user is too close, back up
    # if user is too far away, move forward
    # if user is in the "safe region", stay still
    if front_distance < 2:
        Robot.steer_pair.on(0, -40)
    elif front_distance < 5:
        Robot.steer_pair.on(0, -10)
    elif front_distance > 10:
        Robot.steer_pair.on(0, 20)
    else:
        # otherwise, quit moving
        Robot.steer_pair.off()
