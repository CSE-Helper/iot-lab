import Adafruit_DHT
# Set up the sensor type and GPIO pin
sensor = Adafruit_DHT.DHT11
pin = 4
while True:
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
if humidity is not None and temperature is not None:
print(f"Temperature: {temperature}°C, Humidity: {humidity}%")
else:
print("Failed to read from the DHT sensor.")