import RPi.GPIO as GPIO
import time

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin number
led_pin = 18

# Set up the GPIO pin as an output
GPIO.setup(led_pin, GPIO.OUT)

# Function to turn on the LED
def turn_on():
    GPIO.output(led_pin, GPIO.HIGH)

# Function to turn off the LED
def turn_off():
    GPIO.output(led_pin, GPIO.LOW)

# Main program
try:
    while True:
        turn_on()  # Turn on the LED
        time.sleep(1)  # Wait for 1 second
        turn_off()  # Turn off the LED
        time.sleep(1)  # Wait for 1 second

except KeyboardInterrupt:
    GPIO.cleanup()  # Clean up GPIO on keyboard interrupt
