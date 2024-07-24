import cv2
import numpy as np
from PIL import Image 
path='/home/pi/Downloads/check.jpg'

img=Image.open(path)

size=300, 300
img=img.resize(size,Image.LANCZOS)
#img.info['dpi']
print(img.width)
print(img.height)
img.save("/home/pi/Downloads/resized2.jpg",dpi=(96,96))

