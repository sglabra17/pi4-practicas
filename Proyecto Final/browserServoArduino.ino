//arduino receives data from Pi4
#include <Servo.h>

Servo base;
Servo pinza;

void setup(){
  Serial.begin(9600);
  
  base.attach(9);
  pinza.attach(10);
  
  base.write(0);
  pinza.write(0);
}

void loop(){
  
  if(Serial.available()>0){
    
    String c = Serial.readString();
    Serial.println(c);
    
    if(c=="agarrar"){
      pinza.write(180);
      delay(20);
    }else if(c=="soltar"){
      pinza.write(0);
      delay(20);
    }else{
      base.write(c.toInt());
      delay(20);
    }
    
  }
  
}
