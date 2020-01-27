# Robot.py - Logical definition of the robot with definition of the ports on the EV3 and the sensors / motors connected to it

# Copyright of Viperbots FLL team  http://sites.google.com/view/viperbotsofficial/
# Can be freely used by any developors as long as you inform us on ViperbotsWHMS@gmail.com

# Modified by Shiva Atomatrons under the Viperbots licensing terms

# import misc commands used in the port checker and font setting
from ev3dev2.console import Console
from time import sleep
import sys
from ev3dev2 import DeviceNotFound

# import motor modules and the ev3 ports used for it
from ev3dev2.motor import LargeMotor, MediumMotor, Motor, OUTPUT_B, OUTPUT_C, OUTPUT_A, OUTPUT_D
from ev3dev2.motor import MoveSteering, MoveTank
from ev3dev2.motor import SpeedNativeUnits

# import Sensor modules and the ev3 ports used for it
from ShivaColor import ShivaColor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_4

from ev3dev2.sensor.lego import GyroSensor, TouchSensor, UltrasonicSensor, InfraredSensor
from ev3dev2.sensor import INPUT_3
from ShivaGyro import ShivaGyro

# Creates sound and button objects
from ev3dev2.sound import Sound
from ev3dev2.button import Button

# Sets the font size for robot lcd
console = Console()
console.set_font('Lat15-VGA16.psf.gz')

# Port assignments
MEDIUM_MOTOR_RIGHT = OUTPUT_D
LARGE_MOTOR_LEFT_PORT = OUTPUT_B
LARGE_MOTOR_RIGHT_PORT = OUTPUT_C

TOUCHSENSOR_PORT = INPUT_3
GYROSENSOR_PORT = INPUT_2
ULTRASONIC_PORT = INPUT_1
INFRARED_PORT = INPUT_4

# Checks every port on the robot to see if its connected properly

healthy = False
while healthy == False:
    healthy = True
    try:
        left_wheel = Motor(LARGE_MOTOR_LEFT_PORT)
    except:
        print("BAD LEFT WHEEL")
        healthy = False
    try:
        right_wheel = Motor(LARGE_MOTOR_RIGHT_PORT)
    except:
        print("BAD RIGHT WHEEL")
        healthy = False
    try:
        right_attachment = Motor(MEDIUM_MOTOR_RIGHT)
    except:
        print("BAD RIGHT ATTACHMENT")
        healthy = False

    try:
        ultra = UltrasonicSensor(ULTRASONIC_PORT)
    except:
        print("BAD ULTRASONIC (PORT {})".formatT(ULRASONIC_PORT))
        healthy = False
    try:
        infrared = InfraredSensor(INFRARED_PORT)
    except:
        print("BAD INFRARED (PORT {})".format(INFRARED_PORT))
        healthy = False
    try:
        touch = TouchSensor(TOUCHSENSOR_PORT)
    except:
        print("BAD TOUCH")
        healthy = False
    try:
        gyro = ShivaGyro(GYROSENSOR_PORT)
    except:
        print("BAD GYRO (PORT {})".format(GYROSENSOR_PORT))
        healthy = False
    sleep(0.5)
    console.reset_console()


# Attachment motor direction
CLK_WISE = 'clock_wise'  # positive speed
ANTI_CLK_WISE = 'anti_clck_wise'  # negative speed


# Create objects for the ev3 motors and sensors. Only one object will be created for each physical object and used in every program

# LARGEMOTORS USED FOR WHEELS

# Create object functions for basic movements for wheel pair blocks
steer_pair = MoveSteering(LARGE_MOTOR_LEFT_PORT, LARGE_MOTOR_RIGHT_PORT)
tank_pair = MoveTank(LARGE_MOTOR_LEFT_PORT, LARGE_MOTOR_RIGHT_PORT)

# Create GYROSENSOR
gyro.mode = ShivaGyro.MODE_GYRO_ANG

# Creates sound and button objects
sound = Sound()
button = Button()


# Debug print code

def debug_print(*args, **kwargs):
    '''Print debug messages to stderr.
    This shows up in the output panel in VS Code.
    '''
    print(*args, **kwargs, file=sys.stderr)


# outputs log data to VS Code instead of robot screen
log_file = open('log_data.txt', 'a+')


def log(*args, **kwargs):
    '''Print debug messages to a log file.
    This shows up in the output panel in VS Code.
    '''
    print(*args, **kwargs, file=log_file)
