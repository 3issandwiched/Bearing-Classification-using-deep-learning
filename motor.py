import RPi.GPIO as GPIO
import time
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
i=0
while i<5:
 GPIO.setup(21,GPIO.OUT)
 print ("ON")
 GPIO.output(21,GPIO.HIGH)
 time.sleep(5)
 print ("OFF")
 GPIO.output(21,GPIO.LOW)
 time.sleep(5)
 i+=1
