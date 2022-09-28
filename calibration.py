#Hariharan Mageshanand

from symbol import parameters
import numpy as np
import cv2
import cv2.aruco as aruco
import os
import time
import argparse

data_list=[]
aruco_dict = aruco.Dictionary_get(aruco.DICT_5X5_1000)
board = aruco.GridBoard_create(
    markersX=7,
    markersY=5,
    markerLength=0.03,
    markerSeparation=0.010,
    dictionary=aruco_dict)
parser=argparse.ArgumentParser()
parser.add_argument("-func","--Function",help="enter generate to generate board or calibrate to perform calibration")
parser.add_argument("-in_type","--Input_type",help="Input type it is a video or multiple photos  (enter 'video' for videos and 'image' for multiple images)")
parser.add_argument("-ls","--location",help="enter the location \n (if image put dir) \n (if video put exact video location)")
args=parser.parse_args()
if args.Function:
    if args.Function=="calibrate":
        if args.Input_type and args.location:
            print(args.Input_type)
            if args.Input_type=="video":
                cap=cv2.VideoCapture(args.location)
                while(cap.isOpened()):
                    ret,frame=cap.read()
                    if ret==False:
                        break
                    data_list.append(frame)
            elif args.Input_type=="image":
                files=os.listdir(args.location)
                for i in range(0,len(files)):
                    im=cv2.imread(args.location+"/"+files[i])
                    data_list.append(im)
            else:
                print("it is not a right command please find help :[")
        else:
            print("no argument as been passed")
    elif args.Function=="generate":
        im=board.draw((1920,1080))
        cv2.imwrite("calibration_grid.png",im)
        
    else:
        print("it is not a right command please find help :[")
else:
    print("no argument as been passed")

if args.Function=="calibrate":
    board = aruco.GridBoard_create(
    markersX=7,
    markersY=5,
    markerLength=0.028,
    markerSeparation=0.017,
    dictionary=aruco_dict)
    counter_list=[]
    ids_list=[]
    corners_list=[]
    for i in range(0,len(data_list)):
        #print(corners_list)
        gray=cv2.cvtColor(data_list[i],cv2.COLOR_BGR2GRAY)
        print(gray.shape)
        parameter=aruco.DetectorParameters_create()
        corners,ids,rej_point=aruco.detectMarkers(gray,aruco_dict,parameters=parameter)
        if len(ids)==len(board.ids):
            if len(corners_list)==0:
                corners_list=corners
                ids_list=ids
            else:
                corners_list=np.vstack((corners_list,corners))
                ids_list=np.vstack((ids_list,ids))
            counter_list.append(len(ids))
    counter_list=np.array(counter_list)
    print(corners_list[0])
    print(len(corners_list))
    print(len(counter_list))
    print(len(ids_list))
    ret, mtx, dist, rvecs, tvecs = aruco.calibrateCameraAruco(
            corners_list, 
            ids_list,
            counter_list, 
            board, 
            gray.shape, 
            None, 
            None 
        )
    print(mtx)
    print(dist)
    
