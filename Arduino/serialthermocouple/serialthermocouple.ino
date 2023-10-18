// this example is public domain. enjoy!
// https://learn.adafruit.com/thermocouple/

#include "max6675.h"
#define Iterations 4

int thermoDO = 19;
int thermoCS = 23;
int thermoCLK = 5;
int counter = 0;
float dataarray[Iterations];
float temp = 0;
float T = 0;
int i = 0;

MAX6675 thermocouple(thermoCLK, thermoCS, thermoDO);
void setup() {
  Serial.begin(115200);

  // wait for MAX chip to stabilize
  delay(500);
}

void loop() {
  // basic readout test, just print the current temp
  T = thermocouple.readCelsius();
  if(counter>Iterations+2){
    temp = 0;
    for(i=0;i<Iterations; i++)
    {
      temp += dataarray[i];
    }
    temp = temp/(Iterations);
    Serial.println(temp);
    
    for( i=Iterations - 1;i > 0; i--){
      dataarray[i] = dataarray[i-1]; 
    }
    
    if(T < dataarray[0]*2){
      dataarray[0] = T;
    }
    
  }
  else{
    counter++;
     for( i=Iterations - 1;i > 0; i--){
      dataarray[i] = dataarray[i-1]; 
     }
     dataarray[0] = T;
  }

  
  
  
    
   // For the MAX6675 to update, you must delay AT LEAST 250ms between reads!
   delay(280);
}
