import time
from adafruit_motorkit import MotorKit

'''
TO-DO LIST:
Fix motor numbers for functions
Fix negative numbers (CCW vs CW) for throttle values

'''
kit = MotorKit()


kit.motor1.throttle = 1.0
time.sleep(0.5)
kit.motor1.throttle = 0

def test_motors():
    kit.motor1.throttle = 1.0
    time.sleep(0.5)
    kit.motor1.throttle = 0
    kit.motor2.throttle = 1.0
    time.sleep(0.5)
    kit.motor2.throttle = 0
    kit.motor3.throttle = 1.0
    time.sleep(0.5)
    kit.motor3.throttle = 0
    kit.motor4.throttle = 1.0
    time.sleep(0.5)
    kit.motor4.throttle = 0

def reset_motors():
    kit.motor1.throttle = 0
    kit.motor2.throttle = 0
    kit.motor3.throttle = 0
    kit.motor4.throttle = 0

def left_motors(left_delay, left_throttle):
    kit.motor1.throttle = left_throttle
    kit.motor3.throttle = left_throttle
    time.sleep(left_delay)

def right_motors(right_delay, right_throttle):
    kit.motor2.throttle = right_throttle
    kit.motor4.throttle = right_throttle
    time.sleep(right_delay)

#robot forward
def forward(delay, throttle):    
    left_motors(delay, -throttle)
    right_motors(delay, throttle)
    reset_motors()

#robot backward
def backward(delay, throttle):
    left_motors(delay, throttle)
    right_motors(delay, -throttle)
    reset_motors()

#robot CCW turn
def turn_CCW(delay, throttle):
    left_motors(delay, throttle)
    right_motors(delay, throttle)
    reset_motors()

#robot CW turn
def turn_CW(delay, throttle):
    left_motors(delay, -throttle)
    right_motors(delay, -throttle)
    reset_motors()

