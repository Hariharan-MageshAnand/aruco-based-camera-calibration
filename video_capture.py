#Hariharan_MageshAnand

import cv2
import os
import time
import argparse
parser=argparse.ArgumentParser()
parser.add_argument("-cam","--camera",help="enter the camera ip or int")
parser.add_argument("-o","--out",help="output folder location")
args=parser.parse_args()
ch="0123456789"
if ch.find(args.camera[0])!=-1:
    vid = cv2.VideoCapture(int(args.camera))
else:
    vid=cv2.VideoCapture(args.camera)
os.chdir(args.out)
i=0
while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
    cv2.imwrite("cal_imgs_"+str(i)+".png",frame)
    time.sleep(0.2)
    i=i+1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
