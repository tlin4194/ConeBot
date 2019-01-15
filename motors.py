import time
from adafruit_motorkit import MotorKit

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

#robot forward
def forward():
    kit.motor1.throttle = 1.0
    kit.motor2.throttle = 1.0
    time.sleep(0.5)

#robot backward

#robot CCW turn

#robot CW turn




