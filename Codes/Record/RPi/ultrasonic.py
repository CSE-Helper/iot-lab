import RPi.GPIO as GPIO
import time
TRIG_PIN = 17
ECHO_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)
def measure_distance():
GPIO.output(TRIG_PIN, True)
time.sleep(0.00001)
GPIO.output(TRIG_PIN, False)
while GPIO.input(ECHO_PIN) == 0:
pulse_start = time.time()
while GPIO.input(ECHO_PIN) == 1:
pulse_end = time.time()
pulse_duration = pulse_end - pulse_start
distance = (pulse_duration * 34300) / 2
return distance
try:
while True:
distance = measure_distance()
print(f"Distance: {distance:.2f} cm")
time.sleep(1)
except KeyboardInterrupt:
GPIO.cleanup()