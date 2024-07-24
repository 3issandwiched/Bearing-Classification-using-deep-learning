
def capture(path):
 cam=cv2.VideoCapture(0)
 ret, image=cam.read()

 if ret:
# cv2.imshow('SnapshotTest',image)
  cv2.waitKey(1)
# cv2.destroyWindow('SnapshotTest')
  cv2.imwrite(path,image)
 cam.release()


def resize(path):
 img=Image.open(path)
 size=300, 300
 img=img.resize(size,Image.LANCZOS)
 #img.info['dpi']
 #print(img.width)
 #print(img.height)
 img.save(path,dpi=(96,96))


def output(prediction):
 if(prediction<.5):
  print("DEFECTIVE")
  motor("defective")
 else:
  print("NON DEFECTIVE")
  motor("non defective")

def motor(condition):

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
 if(condition=="defective"):
  forward(6)
 else: 
  reverse(6)
 GPIO.cleanup()


import tensorflow as tf
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image 
from keras.models import load_model
import sys
import time
from time import sleep
import RPi.GPIO as GPIO
a=.5
saved_model=load_model(r"/home/pi/Downloads/final_team8.h5")
path='/home/pi/Desktop/camera/webcam.jpeg'

#zeroth function call
capture(path)

#first function call
resize(path)

img=cv2.imread(path,0)
img=img/255
prediction=saved_model.predict(img.reshape(-1,300,300,1))

#second function call
output(prediction)






































