int smokeSensorPin = A0;
int buzzerPin = 8;
void setup()
{
    pinMode(smokeSensorPin, INPUT);
    pinMode(buzzerPin, OUTPUT);
    Serial.begin(9600);
}
void loop()
{
    int sensorValue = analogRead(smokeSensorPin);
    int threshold = 130;
    if (sensorValue > threshold)
    {
        Serial.println("Smoke detected!");
        digitalWrite(buzzerPin, HIGH);
    }
    else
    {
        Serial.println("No smoke detected.");
        digitalWrite(buzzerPin, LOW);
    }
    delay(1000);
}