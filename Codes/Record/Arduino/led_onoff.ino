int led1 = 0;
int led2 = 1;
int led3 = 2;
int led4 = 3;
int led5 = 4;
void setup()
{
    pinMode(led1, OUTPUT);
    pinMode(led2, OUTPUT);
    pinMode(led3, OUTPUT);
    pinMode(led4, OUTPUT);
    pinMode(led5, OUTPUT);
}
void loop()
{
    digitalWrite(led1, HIGH);
    delay(80);
    digitalWrite(led1, LOW);
    digitalWrite(led2, HIGH);
    delay(80);
    digitalWrite(led2, LOW);
    digitalWrite(led3, HIGH);
    delay(80);
    digitalWrite(led3, LOW);
    digitalWrite(led4, HIGH);
    delay(80);
    digitalWrite(led4, LOW);
    digitalWrite(led5, HIGH);
    delay(80);
    digitalWrite(led5, LOW);
    delay(500);
}