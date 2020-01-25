#!/usr/bin/env micropython
import Robot
import My_block

Robot.gyro.compass_point = 0

Target_Angle = 120
for spins in range(0,293):
	My_block.spin_turn(Target_Angle)
	Target_Angle = Target_Angle + 90