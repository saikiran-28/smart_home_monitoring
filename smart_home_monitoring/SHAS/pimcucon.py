import serial
import RPi.GPIO as GPIO
import time
import json
from random import randint

ser=serial.Serial("/dev/ttyUSB0",9600)  #change ACM number as found from ls /dev/tty/ACM*
ser.baudrate=9600
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
dht={}
while True:
    data=ser.readline()
    a=data.decode('UTF-8')
    temp,hum = a.split('\t')                                                  
    dht["Temp1"]=temp
    dht["Hum1"]=hum.rstrip()
    dht["Temp2"]=randint(0,30)
    dht["Hum2"]=randint(0,50)
    
    print(dht)
    with open("testing.json","w") as outfile:
        json.dump(dht,outfile)
    #print("hell0")
    time.sleep(30)
GPIO.cleanup()
print(type(data))