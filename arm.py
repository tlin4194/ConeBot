import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)

p = GPIO.PWM(13, 50)    # frequency 50 Hz (period 20 ms)
p.start(13)

def arm_release():
    p.ChangeDutyCycle(13)

def arm_down(): #passive grabbing of cone
    p.ChangeDutyCycle(11.5)

def arm_up():
    p.ChangeDutyCycle(3.25)

# p.stop()
# GPIO.cleanup()

arm_down()

