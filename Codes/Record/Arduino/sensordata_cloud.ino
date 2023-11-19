#include <ESP8266WiFi.h>
#include <DHT.h>
const char *ssid = "<Wi-Fi Network Name>";
const char *password = "<Wi-Fi Network Password>";
const char *thingSpeakAPI = "<ThingSpeak Write API Key>";
const int DHTPin = 2;             // GPIO pin to which the DHT sensor is connected
const int UpdateInterval = 30000; // Update data every 30 seconds (in milliseconds)
DHT dht(DHTPin, DHT22);
WiFiClient client;
void setup()
{
    Serial.begin(115200);
    WiFi.begin(ssid, password);
    dht.begin();
}
void loop()
{
    if (WiFi.status() == WL_CONNECTED)
    {
        float temperature = dht.readTemperature();
        if (!isnan(temperature))
        {
            sendTemperatureData(temperature);
        }
    }
    delay(UpdateInterval);
}
void sendTemperatureData(float temp)
{
    if (client.connect("api.thingspeak.com", 80))
    {
        String data = "field1=" + String(temp);
        data += "&status=MQTTPUBLISH"; // Optional status field
        client.println("POST /update HTTP/1.1");
        client.println("Host: api.thingspeak.com");
        client.println("Connection: close");
        client.println("X-THINGSPEAKAPIKEY: " + thingSpeakAPI);
        client.println("Content-Type: application/x-www-form-urlencoded");
        client.print("Content-Length: ");
        client.println(data.length());
        client.println();
        client.print(data);
    }
    else
    {
        Serial.println("Failed to connect to ThingSpeak.");
    }
    client.stop();
}