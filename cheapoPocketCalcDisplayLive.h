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
#ifndef cheapoPocketCalcDisplayLive_h
#define cheapoPocketCalcDisplayLive_h
#include <Arduino.h>

class cheapoPocketCalcDisplayLive
{
  public:  // equals-pin, type-1-pin, type-plus-pin, erase-pin, type-delay, calculate-delay, delay-multiplier
    cheapoPocketCalcDisplayLive(byte ePin, byte t1Pin, byte pPin, byte erPin, int tDelay, int cDelay, int mtpl);
    void writeNumber(unsigned long number);
    void reset();
    void keepAlive();
    boolean isFinished();
void calcDisplayWriteOne();
void calcDisplayWritePlus();
void calcDisplayWriteEqual();
void setMultiplier(int value);
unsigned long milliDelay(unsigned long millseconds);
  private:
// four pins (erase, type1, plus, equal)
long int displayedNumber;
int typeDelay;
int calcDelay;
int multiplier;
void writeItem(int position);
void makeQueue(unsigned long number);
};
#endif

