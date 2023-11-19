#include <SoftwareSerial.h>
SoftwareSerial bluetooth(0, 1); // RX, TX
int ledPin = 9;
char command;
void setup()
{
    pinMode(ledPin, OUTPUT);
    digitalWrite(ledPin, LOW);
    bluetooth.begin(9600);
}
void loop()
{
    if (bluetooth.available() > 0)
    {
        command = bluetooth.read();
        if (command == '1')
        {
            digitalWrite(ledPin, HIGH);
        }
        if (command == '0')
        {
            digitalWrite(ledPin, LOW);
        }
    }
}