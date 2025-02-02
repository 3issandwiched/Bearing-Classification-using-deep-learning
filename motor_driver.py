import sys
import time
from time import sleep
import RPi.GPIO as GPIO

mode=GPIO.getmode()

#GPIO.cleanup()

Forward=26
Backward=20

GPIO.setmode(GPIO.BCM)
GPIO.setup(Forward, GPIO.OUT)
GPIO.setup(Backward, GPIO.OUT)

def forward(x):
 GPIO.output(Forward, GPIO.HIGH)
 print("Moving Forward")
 time.sleep(x)
 GPIO.output(Forward, GPIO.LOW)

def reverse(x):
 GPIO.output(Backward, GPIO.HIGH)
 print("Moving Backward")
 time.sleep(x)
 GPIO.output(Backward, GPIO.LOW)

#while (1):

forward(20)

reverse(20)
GPIO.cleanup()
