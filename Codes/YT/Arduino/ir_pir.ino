// IR

int ir = 7;
int led = 8;
int x;

void setup()
{
    Serial.begin(9600);
    pinMode(7, INPUT);
    pinMode(8, OUTPUT);
}

void loop()
{
    x = digitalRead(ir);
    Serial.println(x);
    delay(300);

    if (x == 1) // Sensor not activated
    {
        digitalWrite(8, LOW);
    }

    else // Sensor Activated[when x is 0]
    {
        digitalWrite(8, HIGH);
    }
}

// PIR
int calibrationTime = 30;
long unsigned int lowIn;
long unsigned int pause = 5000;

boolean lockLow = true;
boolean takeLowTime;

int pirPin = 3; // the digital pin connected to the PIR sensor's output
int ledPin = 13;

// SETUP
void setup()
{
    Serial.begin(9600);
    pinMode(pirPin, INPUT);
    pinMode(ledPin, OUTPUT);
    digitalWrite(pirPin, LOW);
    Serial.print("calibrating sensor ");
    for (int i = 0; i < calibrationTime; i++)
    {
        Serial.print(".");
        delay(1000);
    }
    Serial.println(" done");
    Serial.println("SENSOR ACTIVE");
    delay(50);
}
// LOOP
void loop()
{

    if (digitalRead(pirPin) == HIGH)
    {
        digitalWrite(ledPin, HIGH); // the led visualizes the sensors output pin state
        if (lockLow)
        {
            lockLow = false;
            Serial.println("---");
            Serial.print("motion detected at ");
            Serial.print(millis() / 1000);
            Serial.println(" sec");
            delay(50);
        }
        takeLowTime = true;
    }

    if (digitalRead(pirPin) == LOW)
    {
        digitalWrite(ledPin, LOW); // the led visualizes the sensors output pin state

        if (takeLowTime)
        {
            lowIn = millis();    // save the time of the transition from high to LOW
            takeLowTime = false; // make sure this is only done at the start of a LOW phase
        }
        if (!lockLow && millis() - lowIn > pause)
        {
            lockLow = true;
            Serial.print("motion ended at "); // output
            Serial.print((millis() - pause) / 1000);
            Serial.println(" sec");
            delay(50);
        }
    }
}