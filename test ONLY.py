#!/usr/bin/env micropython 

import My_block
import Robot

My_block.gyro_straight(15, 1)

Robot.right_attachment.on_for_rotations(-20, 0.8)

Robot.tank_pair.on_for_rotations(3, -3, 0.13)

Robot.right_attachment.on_for_rotations(20,1)

Robot.right_attachment.on_for_rotations(-20,0.8)

Robot.tank_pair.on_for_rotations(-3, 3, 0.35)