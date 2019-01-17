import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(19, GPIO.OUT) #12

p = GPIO.PWM(19, 50)  # channel=12 frequency=50Hz
p.start(0)


def arm_down(): #passive grabbing of cone
    p.changeDutyCycle(10) #need to calibrate value
    time.sleep(2)

def arm_up(): 
    p.changeDutyCycle(0) #need to calibrate value
    time.sleep(2)

def main():
    arm_down()
    arm_up()
    p.stop()
    GPIO.cleanup()

main()
