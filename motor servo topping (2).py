# Import library yang diperlukan
import RPi.GPIO as GPIO
import time

# Setup pin servo
GPIO.setwarnings(False)
servo_pin = 5
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

# 50 Hz atau 20 ms periode PWM
pwm = GPIO.PWM(servo_pin, 50)

# Fungsi untuk menggerakkan servo ke posisi tertentu
def move_servo(position):
    duty_cycle = 2 + (position / 18)  # Menghitung duty cycle
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(1)  # Delay 1 detik

try:
    pwm.start(0)  # Inisialisasi servo pada posisi 0 derajat
    print("Starting at zero...")

    while True:
        print("Moving to 180 degrees...")
        move_servo(180)

        print("Moving back to 0 degrees...")
        move_servo(0)

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
    print("Program stopped")
