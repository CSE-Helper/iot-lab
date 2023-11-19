int moistureSensorPin = A0;
int ledPin = 8;
void setup()
{
    pinMode(ledPin, OUTPUT);
    Serial.begin(9600);
}
void loop()
{
    int moistureLevel = analogRead(moistureSensorPin);
    if (moistureLevel < 500)
    {
        digitalWrite(ledPin, HIGH);
        Serial.println("Soil is too dry!");
    }
    else
    {
        digitalWrite(ledPin, LOW);
        Serial.println("Soil moisture is okay.");
    }
    delay(1000);
}