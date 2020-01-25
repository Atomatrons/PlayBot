#!/usr/bin/env micropython

#Checks if medium motor A is ok
try:
    Robot.left_attachment.on(1)
    Robot.left_attachment.off(brake = True)
    print("MOTOR A OK")
    Robot.sound.tone([(392, 350, 100)])

except IOError:
    print("MOTOR A ERROR")
    Robot.sound.tone([(392, 350, 100)])
    Robot.sleep(2)

#Checks if medium motor B is ok
try:
    Robot.right_attachment.on(1)
    Robot.right_attachment.off(brake = True)
    print("MOTOR D OK")
    Robot.sound.tone([(392, 350, 100)])

except IOError:
    print("MOTOR D ERROR")
    Robot.sound.tone([(392, 350, 100)])
    Robot.sleep(2)

try:
    Robot.left_wheel.on(1)
    Robot.left_wheel.off(brake = True)
    print("MOTOR B OK")
    Robot.sound.tone([(392, 350, 100)])

except IOError:
    Robot.sound.tone([(392, 350, 100)])
    print("MOTOR B ERROR")
    Robot.sleep(2)

try:
    Robot.right_wheel.on(1)
    Robot.right_wheel.off(brake = True)
    print("MOTOR C OK")
    Robot.sound.tone([(392, 350, 100)])

except IOError:
    print("MOTOR C ERROR")
    Robot.sound.tone([(392, 350, 100)])
    Robot.sleep(2)



