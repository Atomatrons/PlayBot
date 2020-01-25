#!/usr/bin/env micropython

import Robot
import My_block

Robot.gyro.compass_point = 0

My_block.gyro_straight(20,0.4)

My_block.spin_turn(66)

My_block.gyro_straight(90,7.3)

Robot.left_attachment.on_for_seconds(100, 2)

Robot.steer_pair.on_for_rotations(0, -100, 1)

My_block.spin_turn(0)

My_block.wall_square(-100)

My_block.gyro_straight(30,2.3)

My_block.spin_turn(-28)

My_block.gyro_straight(100,5)