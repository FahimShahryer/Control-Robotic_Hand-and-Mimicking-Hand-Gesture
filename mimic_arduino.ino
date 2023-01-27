#include <Servo.h>
#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>
Adafruit_PWMServoDriver myServo = Adafruit_PWMServoDriver();

#define SERVOMIN 350
#define SERVOMAX 500

int IRSensor = 9;

#define numOfvalRec 5
#define digitPerValRec 1

uint8_t servonum = 0;
uint8_t numberOfServos = 5;


int valsRec[numOfvalRec];

int stringLength = numOfvalRec * digitPerValRec + 1; //$00000
int counter = 0;
bool counterStart = false;  //for counting length
String rString;

void setup() {
  Serial.begin(9600);
  pinMode(IRSensor, INPUT);
  myServo.begin();
  myServo.setPWMFreq(60);
  delay(10);

  myServo.setPWM(0, 0, 500);
  myServo.setPWM(1, 0, 500);
  myServo.setPWM(2, 0, 500);
  myServo.setPWM(3, 0, 500);
  myServo.setPWM(4, 0, 500);
  
}

void rData(){
  while(Serial.available())
  {
    char c = Serial.read();

    if (c == '$'){
      counterStart = true;
    }

     if (counterStart){
      if(counter < stringLength){
        rString = String(rString + c);
        counter++;
      }
      if(counter >= stringLength){
        for (int i = 0; i<numOfvalRec; i++){
          int num = (i*digitPerValRec) + 1;
        valsRec[i] = rString.substring(num,num+digitPerValRec).toInt();
        }
        rString = "";
        counter=0;
        counterStart = false;
      }
    }

  }
}

void loop() {

  // int sensorStatus = digitalRead(IRSensor); // Set the GPIO as Input
  // if (sensorStatus == 1) // Check if the pin high or not
  // {
  //   myServo.setPWM(0, 0, 500);
  //   myServo.setPWM(1, 0, 500);
  //   myServo.setPWM(2, 0, 500);
  //   myServo.setPWM(3, 0, 500);
  //   myServo.setPWM(4, 0, 500);
  // }
  // if (sensorStatus == 0)  {
  //   myServo.setPWM(0, 0, 350);
  //   myServo.setPWM(1, 0, 350);
  //   myServo.setPWM(2, 0, 350);
  //   myServo.setPWM(3, 0, 350);
  //   myServo.setPWM(4, 0, 350);
  // }




  rData();
  if (valsRec[0] == 1)
  {
    myServo.setPWM(0, 0, 350);
  }
  else{
    myServo.setPWM(0, 0, 500);
  }

    if (valsRec[1] == 1)
  {
    myServo.setPWM(1, 0, 350);
  }
  else{
    myServo.setPWM(1, 0, 500);
  }  

   if (valsRec[2] == 1)
  {
    myServo.setPWM(2, 0, 350);
  }
  else{
    myServo.setPWM(2, 0, 500);
  }


    if (valsRec[4] == 1)
  {
    myServo.setPWM(3, 0, 350);
  }
  else{
    myServo.setPWM(3, 0, 500);
  }
    if (valsRec[3] == 1)
  {
    myServo.setPWM(4, 0, 350);
  }
  else{
    myServo.setPWM(4, 0, 500);
  }


}


