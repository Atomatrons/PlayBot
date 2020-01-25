#!/usr/bin/env micropython

# Master_Program: activates our programs based on different button combinations

import Robot
from Anti_Drift_Thing import Anti_Drift_Thing
import My_block
from crane_and_blocks import crane_and_blocks
from runi import push_red_blocks_and_return
from swingset import swingset_mission
from drone import drone

# Runs the gyro drift check program
Anti_Drift_Thing()

#Tells the runners that the program is ready to run
print("READY READY READY READY READY READY READY READY")
Robot.sound.tone([(900, 500, 100)], play_type=1)


# Checks if certain buttons are being pressed
while True:
    Robot.left_wheel.off(brake=False)
    Robot.right_wheel.off(brake=False)
    Robot.left_attachment.off(brake=False)
    Robot.right_attachment.off(brake=False)

    Robot.console.reset_console
    print("READY READY READY READY READY READY READY READY")
    
    if Robot.button.up == True:
        print("RUN 1 RUN 1 RUN 1 RUN 1 RUN 1 RUN 1 RUN 1")
        Robot.sound.tone([(500, 350, 50)], play_type=1)
        for int in range(0, 1400):
            if Robot.button.enter == True:
                print("RUN 1 RUN 1 RUN 1 RUN 1 RUN 1 RUN 1 RUN 1")
                Robot.sleep(0.2)
                crane_and_blocks()
                Robot.console.reset_console()
                print("READY READY READY READY READY READY READY READY")
                Robot.sound.tone([(900, 500, 100)], play_type=1)   

    if Robot.button.down == True:
        print("RUN 2 RUN 2 RUN 2 RUN 2 RUN 2 RUN 2 RUN 2")
        Robot.sound.tone([(500, 350, 50), (500, 350, 50)], play_type=1)
        for int in range(0, 1400):
            if Robot.button.enter == True:
                print("RUN 2 RUN 2 RUN 2 RUN 2 RUN 2 RUN 2 RUN 2")
                Robot.sleep(0.2)
                swingset_mission()
                Robot.console.reset_console()
                print("READY READY READY READY READY READY READY READY")
                Robot.sound.tone([(900, 500, 100)], play_type=1)

    if Robot.button.left == True:
        print("RUN 3 RUN 3 RUN 3 RUN 3 RUN 3 RUN 3 RUN 3")
        Robot.sound.tone([(500, 350, 50), (500, 350, 50), (500, 350, 50)], play_type=1)
        for int in range(0, 1400):
            if Robot.button.enter == True:
                print("RUN 3 RUN 3 RUN 3 RUN 3 RUN 3 RUN 3 RUN 3")
                Robot.sleep(0.2)
                push_red_blocks_and_return()
                Robot.console.reset_console()
                print("READY READY READY READY READY READY READY READY")
                Robot.sound.tone([(900, 500, 100)], play_type=1)

    if Robot.button.right == True:
        print("RUN 4 RUN 4 RUN 4 RUN 4 RUN 4 RUN 4 RUN 4")
        Robot.sound.tone([(500, 350, 50), (500, 350, 50), (500, 350, 50), (500, 350, 50)], play_type=1)
        for int in range(0, 1400):
            if Robot.button.enter == True:
                print("RUN 4 RUN 4 RUN 4 RUN 4 RUN 4 RUN 4 RUN 4")
                Robot.sleep(0.2)
                drone()
                Robot.console.reset_console()
                print("READY READY READY READY READY READY READY READY")
                Robot.sound.tone([(900, 500, 100)], play_type=1)
