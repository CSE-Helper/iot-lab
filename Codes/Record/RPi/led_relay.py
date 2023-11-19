from gpiozero import LED, OutputDevice
from time import sleep
relay = OutputDevice(17, active_high=False)
led = LED(18)
while True:
relay.on()
led.on()
sleep(1)
relay.off()
led.off()
sleep(1)