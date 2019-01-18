import time
from adafruit_motorkit import MotorKit

'''
TO-DO LIST:
Fix motor numbers for functions
Fix negative numbers (CCW vs CW) for throttle values
A = 1
B = 2
C = 3
D = 4

Odd numbered motors are in the front, even numbered in the back
'''
kit = MotorKit()

def test_motors():
    print("testing")
    kit.motor1.throttle = 1.0
    time.sleep(3)
    kit.motor1.throttle = 0
    kit.motor2.throttle = 1.0
    time.sleep(3)
    kit.motor2.throttle = 0
    kit.motor3.throttle = 1.0
    time.sleep(3)
    kit.motor3.throttle = 0
    kit.motor4.throttle = 1.0
    time.sleep(3)
    kit.motor4.throttle = 0

def reset_motors():
    kit.motor1.throttle = 0
    kit.motor2.throttle = 0
    kit.motor3.throttle = 0
    kit.motor4.throttle = 0

def left_motors(left_delay, left_throttle):
    kit.motor1.throttle = left_throttle
    kit.motor2.throttle = left_throttle

def right_motors(right_delay, right_throttle):
    kit.motor3.throttle = right_throttle
    kit.motor4.throttle = right_throttle

def tele_forward():
    reset_motors()
    left_motors(0.1,-1)
    right_motors(0.1,1)

def tele_backward():
    reset_motors()
    left_motors(0.1,1)
    right_motors(0.1,-1)

def tele_turnCCW():
    reset_motors()
    left_motors(0.1,-1)
    right_motors(0.1,-1)

def tele_turnCW():
    reset_motors()
    left_motors(0.1,1)
    right_motors(0.1,1)

def forward(delay, throttle): #move robot forward
    left_motors(delay, throttle)
    right_motors(delay, -throttle)
    time.sleep(delay)
    reset_motors()

def backward(delay, throttle): #move robot backward
    left_motors(delay, -throttle)
    right_motors(delay, throttle)
    time.sleep(delay)
    reset_motors()

def turnCCW(delay, throttle): #turn robot counterclockwise
    left_motors(delay, -throttle)
    right_motors(delay, -throttle)
    time.sleep(delay)
    reset_motors()

def turnCW(delay, throttle): #turn robot clockwise
    left_motors(delay, throttle)
    right_motors(delay, throttle)
    time.sleep(delay)
    reset_motors()

#test_motors()
