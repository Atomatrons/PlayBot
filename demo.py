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
    front_distance = Robot.ultra.distance_inches
    rear_distance = Robot.infrared.proximity
    if rear_distance is None:
        rear_distance = 1000

    if front_distance < 8:
     for int in range (0,5000):
         if rear_distance < 17:
                My_block.spin_turn(90)
    
     while front_distance < 12:
            front_distance = Robot.ultra.distance_inches
            Robot.steer_pair.on(0, 50)
     Robot.steer_pair.off(brake = True)
    
    if rear_distance < 17:
     for int in range (0,5000):
         if front_distance < 8:
             My_block.spin_turn(90)
     while rear_distance < 24:
            rear_distance = Robot.infared.proximity
            Robot.steer_pair.on(0, -50)
     Robot.steer_pair.off(brake = True)

    if front_distance < 4 and rear_distance < 10:
        My_block.spin_turn(90)
        Robot.steer_pair.on_for_rotations(0, 80, 3)
    print (front_distance)
    print (rear_distance)
