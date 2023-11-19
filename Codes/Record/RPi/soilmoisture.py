import RPi.GPIO as GPIO
import time
MOISTURE_SENSOR_PIN = 17
LED_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(MOISTURE_SENSOR_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)
try:
while True:
moisture_level = GPIO.input(MOISTURE_SENSOR_PIN)
if moisture_level == GPIO.LOW:
print("Soil is too dry!")
GPIO.output(LED_PIN, GPIO.HIGH)
else:
GPIO.output(LED_PIN, GPIO.LOW)
time.sleep(1)
except KeyboardInterrupt:
GPIO.cleanup()