#include <dht.h>

dht DHT;

#define DHT11_PIN 7
int Analog_Input = A0;
void setup(){
  pinMode (Analog_Input, INPUT);

  Serial.begin(9600);
}

void loop(){

  
  
  int chk = DHT.read11(DHT11_PIN);
  Serial.print("Temperature - ");
  Serial.println(DHT.temperature);
  Serial.print("Humidity - ");
  Serial.println(DHT.humidity);

  
  int analogValue = analogRead(A4);
  Serial.print("Light - ");
  Serial.println(analogValue); 
  /*
  if(analogValue > 10 && analogValue < 299 )
  {
    Serial.println("Bright - ");
    Serial.println(analogValue); 
  }
  else if(analogValue > 300 && analogValue < 399)
  {
    Serial.println("Light - ");
    Serial.println(analogValue); 
  }
  else if (analogValue > 400 &&  analogValue < 699)
  {
    Serial.println(" - Dim");
    Serial.println(analogValue); 
  }
  else if(analogValue > 700)
  {
    Serial.println(" - Dark");
    Serial.println(analogValue); 
  }
  */
  
  float  Analogous;
  float dbV;
  Analogous  =  analogRead (Analog_Input)   *  (5.0 / 1023.0); 
  dbV = 20*log10(Analogous/0.00923);
  Serial.print  ("Sound - ");
  Serial.println (dbV) ;   
  //Serial.println  ("db");

  float sensor_volt; 
  float RS_gas; 
  float ratio; 
  float R0 = 0.91;

  int sensorValue = analogRead(A2); 
  sensor_volt = ((float)sensorValue / 1024) * 5.0; 
  RS_gas = (5.0 - sensor_volt) / sensor_volt;

  ratio = RS_gas / R0;

  Serial.print("Rs/R0 = "); 
  Serial.println(ratio); 
  

  
  delay(1000);
}
