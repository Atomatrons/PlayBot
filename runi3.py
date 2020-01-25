#!/usr/bin/env micropython

import Robot
import My_block

Robot.gyro.compass_point = -20

My_block.gyro_straight(90,9)

Robot.left_attachment.on_for_seconds(100, 2)

Robot.steer_pair.on_for_rotations(0, -100, 4)

My_block.spin_turn(0)

My_block.wall_square(-100)