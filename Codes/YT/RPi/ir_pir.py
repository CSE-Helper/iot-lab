# IR
import RPi.GPIO as GPIO
import time
PIR_PIN = 17
BUZZER_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
try:
    while True:
        motion = GPIO.input(PIR_PIN)
        if motion == GPIO.HIGH:
            print("Motion detected!")
            GPIO.output(BUZZER_PIN, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(BUZZER_PIN, GPIO.LOW)
            time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()

# PIR
PIR_PIN = 17
LED_PINR = 18
LED_PING = 15
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(LED_PINR, GPIO.OUT)
GPIO.setup(LED_PING, GPIO.OUT)
try:
    while True:
        motion = GPIO.input(PIR_PIN)
        if motion == GPIO.HIGH:
            print("Motion detected!")
            GPIO.output(LED_PINR, GPIO.HIGH)
            GPIO.output(LED_PING, GPIO.LOW)
        else:
            GPIO.output(LED_PINR, GPIO.LOW)
            GPIO.output(LED_PING, GPIO.HIGH)
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
