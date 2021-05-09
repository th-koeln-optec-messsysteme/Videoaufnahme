Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from picamera import PiCamera
from time import sleep

#Initialisiere Kameras
camera1=PiCamera(0)
camera2=PiCamera(1)

#-----------------------Settings------------------------

camera1.awb_mode='horizon'
camera2.awb_mode='horizon'

camera1.video_stabilization=True
camera2.video_stabilization=True

camera1.framerate=24
camera2.framerate=24

camera1.resolution=(1296,972)
camera2.resolution=(1296,972)


#----------------------Aufnahme--------------------------

camera1.start_preview()
sleep(5)
camera1.stop_preview()

camera2.start_preview()
sleep(5)
camera2.stop_preview()


