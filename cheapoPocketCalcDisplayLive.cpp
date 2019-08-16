/*  version 0.01; July, 2016
    CPCdisplay: Driving a cheap pocket calculator using the keys +,CE,= and 1
    Written for:
    hackaday.io/project/12756-a-feature-rich-arduino-waveform-generator
  
    Copyright (C) <2016>  <Joachim Kutzera>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    For a copy of the GNU General Public License
    see <http://www.gnu.org/licenses/>.
*/

#include "cheapoPocketCalcDisplayLive.h"

// special version that allows "multitasking" on the Arduino:
// cp.writenumber() will only write the first character and then return to the executing loop
// each further execution will write another character until the number is finished
// resets when the number changes in the meantime

unsigned long timer;
unsigned long displayedNumber;
unsigned int typeDelay;
unsigned int calcDelay;
byte keyVector[1000] = {0}; // the vector with characters to be pressed
byte erasePin;
byte type1Pin;
byte plusPin;
byte equalPin;
int vecPos = 0;  // the current number of items in the vector
int status = -1; // -1: start, 0 or larger: position in the keyVector

// important note: this is a cycle-wasting millidelay that does not rely on millis() or delay().
// it can be used despite using interrupts elsewhere in your code
// for usage without interrupts, this should be replaced by an actual millis() routine.
// for a naked arduino that does nothing, the multiplier is around 293
unsigned long cheapoPocketCalcDisplayLive::milliDelay(unsigned long millseconds){
  millseconds = millseconds * multiplier;
  unsigned long nl=0;
  digitalWrite(13,1);
  for (long a=0;a<millseconds;a++)
      nl = nl + a*a;
  digitalWrite(13,0);
  for (long a=0;a<millseconds;a++)
	nl = nl + a*a;
  return (nl);
  }

void cheapoPocketCalcDisplayLive::reset(){
  digitalWrite(erasePin,1);
    milliDelay(typeDelay);
  digitalWrite(erasePin,0);
    milliDelay(typeDelay);
  displayedNumber = 99999999;
  }

boolean cheapoPocketCalcDisplayLive::isFinished(){
  return (status == vecPos);
  }

void cheapoPocketCalcDisplayLive::setMultiplier(int value){
  multiplier = value;
  }

void cheapoPocketCalcDisplayLive::calcDisplayWriteOne(){
    //Serial.println("one");
    digitalWrite(type1Pin,1);
    milliDelay(typeDelay/2);
    digitalWrite(type1Pin,0);
    milliDelay(typeDelay);
  }

void cheapoPocketCalcDisplayLive::calcDisplayWritePlus(){
    //Serial.println("+");
    digitalWrite(plusPin,1);
    milliDelay(calcDelay/2);
    digitalWrite(plusPin,0);
    milliDelay(calcDelay);
  }
  
  void cheapoPocketCalcDisplayLive::calcDisplayWriteEqual(){
    //Serial.println("=");
    digitalWrite(equalPin,1);
    milliDelay(calcDelay);
    digitalWrite(equalPin,0);
    milliDelay(calcDelay);
  }

void cheapoPocketCalcDisplayLive::writeItem(int keyValue){
  //Serial.print("writeitem ");
  //Serial.println(keyValue);
  if (keyValue==0) reset();
  if (keyValue==1) calcDisplayWriteOne();
  if (keyValue==2) calcDisplayWritePlus();
  if (keyValue==3) calcDisplayWriteEqual();    
  }

void addToQueue(int item){
  keyVector[vecPos] = item;
  vecPos ++;
  }

// reminder: four pins (erase, type1, plus, equal)
//                        0       1     2     3
void cheapoPocketCalcDisplayLive::makeQueue(unsigned long number){
  unsigned long dnum = number; 
  vecPos = 0;
  if (dnum==1){
    addToQueue(1);
    }
  else {
    unsigned long onePiece = 0;
    byte numOnes = 0;
    byte numOnesOld = 0;
    boolean inEqualMode = false; // before starting to press = repeatedly, it must be pressed once more
    addToQueue(2); // a initial +
    while (dnum > 0){
        onePiece = 0;
        numOnes = 0;
        while (onePiece <= dnum){ // how many 111s are still smaller?
          onePiece = onePiece * 10 + 1;
          numOnes++;
          }
        numOnes--;
        dnum = dnum - onePiece/10;   
        if (numOnesOld > 0)
          if (numOnesOld != numOnes)
            addToQueue(2);  // the + from the last letter
        if (numOnesOld == numOnes){ // i only need to press "=" once more, happens also when only single 1s are left
            if (!inEqualMode)
              addToQueue(3); // =, because the + wasn't pressed
            addToQueue(3); // now the other =s
            inEqualMode = true;
            }
        else { // more than one 1 and a different number than last time
          if (inEqualMode)
             addToQueue(2); // after a "=" row, a plus needs to be pressed before the next 1
          inEqualMode = false; 
          for (byte a=0;a<numOnes;a++)
		 addToQueue(1);
          }
        numOnesOld = numOnes;  
        } 
    }  
  addToQueue(2); // one last +
  }

void cheapoPocketCalcDisplayLive::writeNumber(unsigned long number){
  if (number != displayedNumber){ // starting over
    if ( (status == vecPos) & (number > displayedNumber) ){
	  makeQueue(number - displayedNumber);
      }
    else {
      reset();
      makeQueue(number);
      }
    status = 0;
    displayedNumber = number;
    }
    if (status < vecPos){
      writeItem(keyVector[status]);
      status ++;
    } 
}

cheapoPocketCalcDisplayLive::cheapoPocketCalcDisplayLive(byte ePin, byte t1Pin, byte pPin, byte erPin, int tDelay, int cDelay, int mtpl){
  erasePin = erPin; // pin of the erase button
  type1Pin = t1Pin; // pin to type 1
  plusPin = pPin; // pin to type +
  equalPin = ePin; // pin to type =
  pinMode(erasePin, OUTPUT);  
  pinMode(type1Pin, OUTPUT);  
  pinMode(plusPin, OUTPUT);
  pinMode(equalPin, OUTPUT);
  typeDelay = tDelay; // delay for typing
  calcDelay = cDelay; // delay for a addition (on some calcs, additions go a bit slower than typing)
  multiplier = mtpl; // multiplier for the two delays (speeding up/down the display without changing the two delay values while running)
  displayedNumber = 99999999;
  }
