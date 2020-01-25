#!/usr/bin/env micropython
import Robot
import My_block

Robot.gyro.compass_point = 0

My_block.gyro_straight(30, 1)

My_block.spin_turn(343)

My_block.spin_turn(45)

My_block.spin_turn(90)