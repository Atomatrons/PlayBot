#!/usr/bin/env micropython
import My_block
import Robot
"""
This is mission 11 and 12 and it scores 95 points. This is Kyan and Rushil's mission.
"""

def push_red_blocks_and_return():
    """
    Pushes red blocks to the red circle then returns to base.
    """
    Robot.gyro.compass_point = 75
    Robot.tank_pair.on_for_rotations(50, 50, 3.9)
    Robot.tank_pair.on_for_rotations(50, 50, -1.5)
    My_block.spin_turn(90)
    My_block.wall_square(100)
