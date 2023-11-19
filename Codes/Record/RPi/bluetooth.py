import bluetooth
from gpiozero import LED
import time
led = LED(17) # Change to the GPIO pin you are using
server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
port = 1
server_sock.bind(("", port))
server_sock.listen(1)
print("Waiting for a Bluetooth connection...")
client_sock, address = server_sock.accept()
print("Accepted connection from", address)
try:
while True:
data = client_sock.recv(1024).decode('utf-8')
if not data:
break
if data == "on":
led.on()
elif data == "off":
led.off()
except KeyboardInterrupt:
pass
client_sock.close()
server_sock.close()