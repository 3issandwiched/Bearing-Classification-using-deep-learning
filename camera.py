import cv2
cam=cv2.VideoCapture(0)
ret, image=cam.read()

if ret:
 cv2.imshow('SnapshotTest',image)
 cv2.waitKey(10)
 cv2.destroyWindow('SnapshotTest')
 cv2.imwrite('/home/pi/Desktop/webcam.jpeg',image)
cam.release()
