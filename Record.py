from picamera import PiCamera
from time import sleep
import datetime

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

log=open('/home/pi/Documents/Log.txt','a')
log.write("\n"+"Start"+"\n")
log.close()

i=0
while(True):
    i+=1
    stamp=datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

    if i==1:
        camera1.start_recording("/home/pi/Videos/Cam1/cam1_"+stamp+".h264")
        sleep(5)
        stamp=datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
        camera2.start_recording("/home/pi/Videos/Cam2/cam2_"+stamp+".h264")

    if i>1:
        camera1.split_recording("/home/pi/Videos/Cam1/cam1_"+stamp+".h264")
        sleep(5)
        stamp=datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
        camera2.split_recording("/home/pi/Videos/Cam2/cam2_"+stamp+".h264")


    sleep(600)

    #Log
    print(datetime.datetime.now().time())
    log=open('/home/pi/Documents/Log.txt','a')
    log.write(str(i)+" - "+datetime.datetime.now().strftime("%H:%M:%S")+"\n")
    log.close()
