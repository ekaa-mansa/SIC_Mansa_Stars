# Title: SG90 Servo Driver Code - RPi.GPIO
# Author: donskytech

import RPi.GPIO as GPIO
import time

# Setup RPi
GPIO.setwarnings(False)
servo_pin = 6
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

# 50 Hz or 20 ms PWM period
pwm = GPIO.PWM(servo_pin, 50)

print("Starting at zero...")
pwm.start(5)

try:
    while True:
        print("Setting to 10...")
        pwm.ChangeDutyCycle(10)
        time.sleep(1)

        print("Setting to 5...")
        pwm.ChangeDutyCycle(5)
        time.sleep(1)
        # Menunggu 5 detik
        time.sleep(7)
        
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
    print("Program stopped")
