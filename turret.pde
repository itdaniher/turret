// Import the Arduino Servo library
#include <Servo.h> 

// Create a Servo object for each servo
Servo servo;

// Common servo setup values
int minPulse = 600;	 // minimum servo position, us
int maxPulse = 2400;	// maximum servo position, us

// User input for servo and position
int userInput[3];		// raw input from serial buffer, 3 bytes
int startbyte;			 // start byte, begin reading input
int val;
int state;
int i;							 // iterator

int uvPin = 4;
int triggerPin = 8;
int hPinA = 6;
int hPinB = 7;

void setup() 
{ 
  // Attach each Servo object to a digital pin
  servo.attach(3, minPulse, maxPulse);
  pinMode(triggerPin, OUTPUT);
  pinMode(uvPin, OUTPUT);

  Serial.begin(115200);
} 

void loop() 
{ 
  if (Serial.available() > 2) {
    startbyte = Serial.read();
    if (startbyte == 255) {
      for (i=0;i<2;i++) {
        userInput[i] = Serial.read();
      }
      val = userInput[0];
      state = userInput[1];
      if (state == 255) { 
        val = 255; 
      }

      switch (val) {
      case 1:
        servo.write(state);
        break;
      case 2:
        digitalWrite(triggerPin, state);
        break;
      case 3:
        digitalWrite(uvPin, state);
        break;
      case 4:
        digitalWrite(hPinA, state);
        break;
      case 5:
        digitalWrite(hPinB, state);
        break;
      }
    }
  }


}








