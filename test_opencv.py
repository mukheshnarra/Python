# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 09:32:18 2019

@author: MUKHESH
"""

import cv2
import os

file_name='video.mp4'
my_res='480p'
frames_second=24
STD_DIMENSION={'480p':(640,480),'1028p':(1920,1080),'720p':(1280,720)}
VIDEO_FORMAT={'avi':cv2.VideoWriter_fourcc(*'XVID'),'mp4':cv2.VideoWriter_fourcc(*'H264')}
def change_dim(cap,width,height):
    cap.set(3,width)
    cap.set(4,height)

def rescale(frame,scale=75):
    width=int(frame.shape[1]*scale/100)
    height=int(frame.shape[0]*scale/100)
    return cv2.resize(frame,(width,height))

def get_dim(cap,res=my_res):
    width,height=STD_DIMENSION['480p']
    if res in STD_DIMENSION:
        width,height=STD_DIMENSION[res]
    change_dim(cap,width,height)
    return (width,height)


def get_format(file_name):
    filename,ext=os.path.splitext(file_name)
    if ext in VIDEO_FORMAT:
        return VIDEO_FORMAT[ext]
    return VIDEO_FORMAT['avi']
        

cap=cv2.VideoCapture(0)
#change_dim(cap,2040,1080)

dim=get_dim(cap,my_res)
video_format=get_format(file_name)
out=cv2.VideoWriter(file_name,video_format,frames_second,dim)
while True:
    i,frame = cap.read()
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    out.write(frame)
#    grey=rescale(grey,25)
    cv2.imshow('test',frame)
    cv2.imshow('grey',grey)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

out.release() 
cap.release()
cv2.destroyAllWindows()