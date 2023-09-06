from guizero import App, Box, PushButton
import RPi.GPIO as GPIO
import time

# Konfigurasi pin GPIO
STEP_PIN = 9
DIR_PIN = 10

# Inisialisasi GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(STEP_PIN, GPIO.OUT)
GPIO.setup(DIR_PIN, GPIO.OUT)

# Fungsi untuk menggerakkan motor stepper
def move_stepper(steps, direction):
    # Mengatur arah motor
    if direction == "CW":
        GPIO.output(DIR_PIN, GPIO.LOW)
    elif direction == "CCW":
        GPIO.output(DIR_PIN, GPIO.HIGH)

    # Menggerakkan motor dengan langkah-langkah yang ditentukan
    for _ in range(steps):
        GPIO.output(STEP_PIN, GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(STEP_PIN, GPIO.LOW)
        time.sleep(0.001)

# Fungsi yang akan dipanggil saat tombol "Langkah CW" ditekan
def step_cw():
    move_stepper(533, "CW")

# Fungsi yang akan dipanggil saat tombol "Langkah CCW" ditekan
def step_ccw():
    move_stepper(533, "CCW")

# Membuat GUI menggunakan guizero
app = App("Kontrol Motor Stepper")
box = Box(app, layout="grid")

# Tombol "Langkah CW"
button_cw = PushButton(box, text="Cup Sealer Masuk", command=step_cw, grid=[0, 0])

# Tombol "Langkah CCW"
button_ccw = PushButton(box, text="Cup Sealer Keluar", command=step_ccw, grid=[1, 0])

# Menjalankan aplikasi
app.display()
