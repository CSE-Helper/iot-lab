// IR
int pirPin = 2;
int ledPin = 8;
void setup()
{
    pinMode(pirPin, INPUT);
    pinMode(ledPin, OUTPUT);
    Serial.begin(9600);
}
void loop()
{
    int motion = digitalRead(pirPin);
    if (motion == HIGH)
    {
        digitalWrite(ledPin, HIGH);
        delay(200);
        digitalWrite(ledPin, LOW);
        delay(200);
    }
    Serial.println(motion);
    delay(100);
}

// PIR
int pirPin = 2;
int buzzerPin = 8;
void setup()
{
    pinMode(pirPin, INPUT);
    pinMode(buzzerPin, OUTPUT);
    Serial.begin(9600);
}
void loop()
{
    int motion = digitalRead(pirPin);
    if (motion == HIGH)
    {
        delay(1000);
        digitalWrite(buzzerPin, LOW);
    }
    Serial.println(motion);
    delay(100);
}