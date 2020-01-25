#!/usr/bin/env micropython

import Robot
import My_block

def drone():
    Robot.gyro.compass_point = 0

    My_block.gyro_straight(30, 2.43)

    My_block.spin_turn(45)

    My_block.gyro_straight(30, 2.1)

    My_block.line_square(20, 20)

    My_block.gyro_straight(20, 0.58)

    Robot.right_attachment.on_for_rotations(-100, 4.9)

    My_block.gyro_straight(10, 0.3)

    My_block.spin_turn(30)

    Robot.right_attachment.on_for_rotations(100, 2.3)

    My_block.gyro_straight(-10, 1)

    My_block.wall_square(-100)

    Robot.right_attachment.on_for_seconds(40, 5)
