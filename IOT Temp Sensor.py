int x = 1;
int ledR = 2;
int ledR1 = 3;
int ledR2 = 4;
float Volt = 0.0;
float tempC = 0.0; 
float tempF = 0.0;
float count = 0;
double tempAV = 0;
double tempT = 0;
int tempS = 0;

int HOT()
{
  Serial.println("!!!WARNING HOT!!!");
  digitalWrite(ledR1, HIGH);
  delay(1000);
  digitalWrite(ledR1, LOW);
  delay(1000);
}
int COLD()
 { 
   Serial.println("!!!WARNING COLD!!!");
   digitalWrite(ledR2, HIGH);
   delay(1000);
   digitalWrite(ledR2, LOW);
   delay(1000);
 }
int NORMAL()
 {
   	Serial.println("**NORMAL**");
    digitalWrite(ledR, HIGH);
    delay(1000);
    digitalWrite(ledR, LOW);
    delay(1000);
 }
void setup()
{
  Serial.begin(9600);
}

void loop()
{
  for (int x = 1; x < 1000; x++); {
    tempS = analogRead(A0);
    Volt = tempS/1023.0 * 5.00 * 1000;
    tempC = (Volt - 500) / 10;
    //Serial.println(tempC);
    tempT = tempC + x;
    //Serial.println(tempT);
    tempAV = tempT / x;
    //Serial.println(tempAV);
  }
    
    tempF = tempAV * 1.8 + 32;
    Serial.println("Average Temp:  ");
    Serial.print(tempF);
    Serial.println(" F");
    //Serial.println("Average Temp:");
    //Serial.print(tempAV);
    //Serial.println(" C");
  
  if (tempF >= 90)
    {
    HOT();
	}
  
  else if (tempF <= 32)
    { 
    COLD();
	}
  
  else 
    { 
	NORMAL();
	}
}
