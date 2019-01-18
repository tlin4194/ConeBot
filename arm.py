import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT) #12

p = GPIO.PWM(18, 50)  # channel=12 frequency=50Hz
p.start(7.5)

def arm_release():
    p.ChangeDutyCycle(3) # (0.8 ms / 20 ms)

def arm_down(): #passive grabbing of cone
    p.ChangeDutyCycle(4)

def arm_up():
    p.ChangeDutyCycle(12) # (2.2 ms / 20 ms)

def main():
    arm_down()
    arm_up()
    p.stop()
    GPIO.cleanup()

