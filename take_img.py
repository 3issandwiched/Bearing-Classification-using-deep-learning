import cv2
import numpy as np
from PIL import Image 
cam=cv2.VideoCapture(0)
ret, image=cam.read()

x=input()
y='/home/pi/Desktop/training_images/'
z='.jpeg'
a=1


while a<11:
 if ret:
  #cv2.imshow('SnapshotTest',image)
  cv2.waitKey(10)
 # cv2.destroyWindow('SnapshotTest')

  cv2.imwrite(y+str(x)+z,image)
 cam.release()
 img=Image.open(y+str(x)+z)
 size=300, 300
 img=img.resize(size,Image.LANCZOS)
 img.save(y+str(x)+z,dpi=(96,96))
 x=int(x)+1
 a=a+1

#/home/pi/Desktop/training_images
