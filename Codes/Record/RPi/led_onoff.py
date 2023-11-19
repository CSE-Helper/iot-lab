import RPi.GPIO as GPIO
import time
LED_PIN1 = 14
LED_PIN2 = 15
LED_PIN3 = 18
LED_PIN4 = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN1, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)
GPIO.setup(LED_PIN3, GPIO.OUT)
GPIO.setup(LED_PIN4, GPIO.OUT)
try:
while True:
val = int(input(“Enter value between 1 to 4 :::”))
if(val == 1){
GPIO.output(LED_PIN1, GPIO.HIGH)
GPIO.output(LED_PIN2, GPIO.LOW)
GPIO.output(LED_PIN3, GPIO.LOW)
GPIO.output(LED_PIN4, GPIO.LOW)
time.sleep(2)
}
if(val == 2){
GPIO.output(LED_PIN1, GPIO.LOW)
GPIO.output(LED_PIN2, GPIO.HIGH)
GPIO.output(LED_PIN3, GPIO.LOW)
GPIO.output(LED_PIN4, GPIO.LOW)
time.sleep(2)
}
if(val == 3){
GPIO.output(LED_PIN1, GPIO.LOW)
GPIO.output(LED_PIN2, GPIO.LOW)
GPIO.output(LED_PIN3, GPIO.HIGH)
GPIO.output(LED_PIN4, GPIO.LOW)
time.sleep(2)
}
if(val == 4){
GPIO.output(LED_PIN1, GPIO.LOW)
GPIO.output(LED_PIN2, GPIO.LOW)
GPIO.output(LED_PIN3, GPIO.LOW)
GPIO.output(LED_PIN4, GPIO.HIGH)
time.sleep(2)
}
if(val > 4){
GPIO.output(LED_PIN1, GPIO.LOW)
GPIO.output(LED_PIN2, GPIO.LOW)
GPIO.output(LED_PIN3, GPIO.LOW)
GPIO.output(LED_PIN4, GPIO.LOW)
time.sleep(2)
}
except KeyboardInterrupt:
GPIO.cleanup()