import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
sensor_pin = 18
buzzer_pin = 17
GPIO.setup(sensor_pin, GPIO.IN)
GPIO.setup(buzzer_pin, GPIO.OUT)
try:
while True:
if GPIO.input(sensor_pin):
print("Gas/smoke detected!")
GPIO.output(buzzer_pin, GPIO.HIGH)
else:
print("No gas/smoke detected.")
GPIO.output(buzzer_pin, GPIO.LOW)
time.sleep(1)
except KeyboardInterrupt:
GPIO.cleanup()