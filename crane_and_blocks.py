#!/usr/bin/env micropython
import Robot
import My_block

def crane_and_blocks():
    """Test"""
    Robot.gyro.compass_point = 0

    My_block.gyro_straight(30, 2.2)

    My_block.gyro_straight(-50, 0.9)

    My_block.spin_turn(90)

    My_block.gyro_straight(20, 0.95)
    
    My_block.spin_turn(0)

    My_block.gyro_straight(20,2.1)

    Robot.sleep(0.3)

    My_block.wall_square(-100)

    My_block.gyro_straight(20, 0.2)

    My_block.spin_turn(-40)

    Robot.steer_pair.on_for_rotations(0, 100, 3.9)