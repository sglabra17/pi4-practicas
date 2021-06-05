#include <Servo.h>

Servo motor;
int pos = 0;

void setup(){
  Serial.begin(9600);
  motor.attach(9);
  motor.write(0);
}

void loop(){
  if(Serial.available()>0){
    String c = Serial.readString();
    
    switch(c.toInt()){
      case   1:
             motor.write(0);
             delay(20);
             break;
      case   2:
             motor.write(90);
             delay(20);
             break;
      case   3:
             motor.write(180);
             delay(20);
             break;
      case   4:
             for(pos=0;pos<180;pos++){
                motor.write(pos);//grados -> importante
                delay(20);//retardo ->importante
              }
              for(pos=180;pos>0;pos--){
                motor.write(pos);
                delay(20);
              }
              break;
    }
  }
}
