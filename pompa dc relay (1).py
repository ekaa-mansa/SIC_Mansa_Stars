import RPi.GPIO as GPIO
import time

# Set mode GPIO ke BCM
GPIO.setmode(GPIO.BCM)

# Tentukan pin yang digunakan untuk masing-masing relay
RELAY1_PIN = 14
RELAY2_PIN = 15
RELAY3_PIN = 18
RELAY4_PIN = 23

# Inisialisasi pin relay sebagai OUTPUT
GPIO.setup(RELAY1_PIN, GPIO.OUT)
GPIO.setup(RELAY2_PIN, GPIO.OUT)
GPIO.setup(RELAY3_PIN, GPIO.OUT)
GPIO.setup(RELAY4_PIN, GPIO.OUT)

# Matikan semua relay saat awalnya
GPIO.output(RELAY1_PIN, GPIO.LOW)
GPIO.output(RELAY2_PIN, GPIO.LOW)
GPIO.output(RELAY3_PIN, GPIO.LOW)
GPIO.output(RELAY4_PIN, GPIO.LOW)

try:
    # Contoh penggunaan relay: hidupkan Relay 1 selama 5 detik
    GPIO.output(RELAY1_PIN, GPIO.HIGH)
    time.sleep(5)  # Tunggu selama 5 detik
    GPIO.output(RELAY1_PIN, GPIO.LOW)

    # Ulangi proses untuk Relay 2, Relay 3, dan Relay 4 sesuai kebutuhan Anda
    # Anda dapat menyesuaikan logika pengendalian relay sesuai dengan kebutuhan aplikasi Anda.

except KeyboardInterrupt:
    # Matikan semua relay dan bersihkan pin GPIO saat program dihentikan
    GPIO.output(RELAY1_PIN, GPIO.LOW)
    GPIO.output(RELAY2_PIN, GPIO.LOW)
    GPIO.output(RELAY3_PIN, GPIO.LOW)
    GPIO.output(RELAY4_PIN, GPIO.LOW)
    GPIO.cleanup()
