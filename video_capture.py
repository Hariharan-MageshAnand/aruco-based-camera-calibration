#Hariharan_MageshAnand

import cv2
import os
import time
import argparse
parser=argparse.ArgumentParser()
parser.add_argument("-cam","--camera",help="enter the camera ip or int")
parser.add_argument("-o","--out",help="output folder location")
args=parser.parse_args()
vid = cv2.VideoCapture(args.camera)
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
