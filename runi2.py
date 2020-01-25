#!/usr/bin/env micropython
import Robot
import My_block

def push_tan_block_return():
    """ 
    This is the tan block pushing mission and it scores 60 points. This is Kyan and Rushil's second mission.
    """
    Robot.gyro.compass_point = 0
    
    #Robot.tank_pair.on_for_rotations(50, 50, 4)
    #Robot.tank_pair.on_for_rotations(50, 50, -2.75)
    Robot.tank_pair.on_for_rotations(50, 50, 2.9)
    
    Robot.tank_pair.on_for_rotations(50, 50, -2.25)
    
    My_block.spin_turn(90)
    My_block.wall_square(100)
