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






















