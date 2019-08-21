normal = '\033[0m'
kirmizi= '\033[31m'
yesil= '\033[32m'
sari= '\033[33m'
lacivert= '\033[34m'
mor= '\033[35m'
mavi= '\033[36m'
pmavi = '\033[96m'#p --> parlak
pkirmizi= '\033[91m'
pyesil = '\033[92m'
psari = '\033[93m'
siyah = '\033[90m'
asiyah= '\033[40m'#a --> arkaplan
akirmizi= '\033[41m'
ayesil= '\033[42m'
asari= '\033[43m'
alacivert= '\033[44m'
amor= '\033[45m'
amavi= '\033[46m'
abeyaz= '\033[47m'
apsiyah= '\033[100m'#a --> arkaplan-parlak
apkirmizi= '\033[101m'
apyesil= '\033[102m'
apsari= '\033[103m'
aplacivert= '\033[104m'
apmor= '\033[105m'
apmavi= '\033[106m'
apbeyaz= '\033[107m'







import serial
ard = serial.Serial('/dev/ttyUSB0')
#ard.write()

#menu1
print(psari , "Islem Seciniz: ")
print(pmavi ," 1 - PWM-Servo/ESC ureteci")
print(pmavi ,"2 - PWM ureteci(Duty Cycle)")
print(pmavi ,"3 - Dalga jeneratorü")
print(pmavi ,"4 - PWM ölçer")

menu1 = input()

if (menu1 == 1):
	#menu2
	print(pyesil ,"1 - Manual")
	print(pyesil ,"2 - Sweep")
	print(pyesil ,"3 - ESC Başlatıcı")
	if(menu2 == 1):
		#frekans = input("Frekansı gitriniz (Hz): ")
		sure = input("Acik kalma suresini giriniz(800-2500) : ")
		ard.write(1)
		ard.write(sure)

	if(menu2 == 2):
		ard.write(2)
		aah == input("Artıs-Azalıs hızını girin (Milisecond) : ")
	
	if(menu2 == 3):
		ard.write(3)

if(menu1 == 2):
	duty = input("Duty Cycle giriniz (%) : ")
	ard.write(4)
	ard.wrtite(dc)
        frekans = input("Frekansı gitriniz (Hz): ")
	ard.write(frekans)


if(menu1 == 3):
	#menu3
	print("Dalga türünü secin : ")
	print(pyesil ,"1 - Kare")
	print(pyesil ,"2 - Sinus")
	print(pyesil ,"3 - Ucgen")	
	menu3 = input()
	frekans = input("Frekansı gitriniz (Hz): ")

	if(menu3 == 1):
		ard.write()

	if(menu3 == 2):	
		ard.write()

	if(menu3 == 3):	
		ard.write()

	ard.write(frekans)






void setup ()
{
  pinMode (3, OUTPUT) ;
  TCCR2A = 0x23 ;
  TCCR2B = 0x09 ; // mode 7, clock prescale by 1
  OCR2A = 160-1 ;  // 160 clock periods = 10us per cycle
  OCR2B =0 ;
  TCNT2 =0 ;
}

void loop ()
{
  // here you can set the duty cycle by writing values between 0 and 160 to 
  // OCR2B
}






void arduino_FastPWM()
{
  // This will activate a PWM frequency of 62500 Hz on the 
  // PWM pins associated with Timer1
  // Arduino UNO ==> pin-9 and pin-10
  // Arduino MEGA ==>  pin-11 and pin-12
#if defined(__AVR_ATmega328P__)
  analogWrite(9,127); // let Arduino do PWM timer and pin initialization
#elif defined(__AVR_ATmega1280__) || defined(__AVR_ATmega2560__)  
  analogWrite(11,100); // // let Arduino do PWM timer and pin initialization
#else
  *** wrong board ***
#endif  
  // finally set fast-PWM at highest possible frequency
  TCCR1A = _BV(COM1A1) | _BV(WGM10);
  TCCR1B = _BV(CS10) | _BV(WGM12);
}

#include <avr/io.h>
#include <util/delay.h>

int main(void)
{
  pinMode(3, OUTPUT); // Output pin for OCR2B
  pinMode(5, OUTPUT); // Output pin for OCR0B

  // Set up the 250 kHz output (but cro measures only 125 kHz)
   TCCR2A = _BV(COM2A1) | _BV(COM2B1) | _BV(WGM21) | _BV(WGM20);
   TCCR2B = _BV(WGM22) | _BV(CS20);
   OCR2A = 63;
   OCR2B = 0;

  // Set up the 8 MHz output
   TCCR0A = _BV(COM0A1) | _BV(COM0B1) | _BV(WGM01) | _BV(WGM00);
   TCCR0B = _BV(WGM02) | _BV(CS00);
   OCR0A = 1;
   OCR0B = 0;


  // Make the 250 kHz rolling
  while (1) {
    _delay_us(5);
    if (OCR2B < 63)
      OCR2B += 5;
    else
      OCR2B = 0;
  }
}




  pinMode(3, OUTPUT);
  pinMode(11, OUTPUT);
  TCCR2A = _BV(COM2A1) | _BV(COM2B1) | _BV(WGM21) | _BV(WGM20);
  TCCR2B = _BV(CS22);
  OCR2A = 180;
  OCR2B = 50;




pinMode(3, OUTPUT);
  pinMode(11, OUTPUT);
  TCCR2A = _BV(COM2A1) | _BV(COM2B1) | _BV(WGM20);
  TCCR2B = _BV(CS22);
  OCR2A = 180;
  OCR2B = 50;

	
	
	
	void setup() {

// put your setup code here, to run once:

noInterrupts();

TCCR2A = 0; // clear out the timer2 registers

TCCR2B = 0;

TCNT2 = 0; // initialize the counter at 0

OCR2A = 80; // corresponds to 100kHz signal using no prescaler

TCCR2A |= (1 << WGM21); // CTC mode for timer 2

TCCR2B |= (1 << CS20); // no prescaler - running off 16MHz clock

TIMSK2 |= (1 << OCIE2A);

interrupts();

}

ISR(TIMER2_COMPA_vect) // timer compare interrupt service routine

{

PORTD = PORTD ^ 0b00001000; // toggle digital out pin 3

}

void loop() {

// put your main code here, to run repeatedly:

}
	
	
	



















