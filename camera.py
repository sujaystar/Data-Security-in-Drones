# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 10:45:58 2019

@author: Sujay022199
"""

import cv2
import random
#import os
# Camera 0 is the integrated web cam on my netbook
camera_port = 0
 
#Number of frames to throw away while the camera adjusts to light levels
ramp_frames = 30
 
# Now we can initialize the camera capture object with the cv2.VideoCapture class.
# All it needs is the index to a camera port.
camera = cv2.VideoCapture(camera_port)
 
# Captures a single image from the camera and returns it in PIL format
def get_image():
    camera = cv2.VideoCapture(camera_port)
    retval, im = camera.read()
    return im


builds="C:\\Users\\Sujay022199\\.spyder-py3\\building"
cars="C:\\Users\\Sujay022199\\.spyder-py3\\car"
flowers="C:\\Users\\Sujay022199\\.spyder-py3\\flower"
path=[builds,cars,flowers]
print('Enter your preference')
print('1.building')
print('2.car')
print('3.flower')
p=eval(input())
if p==1:
    paths=path[0]
elif p==2:
    paths=path[1]
else:
    paths=path[2]
#files=os.listdir(paths)
#for i in files:
    #print(i)
 # read is the easiest way to get a full image out of a VideoCapture object.
   #retval, im = camera.read()
   #return im
#index=random.randint(1,1000)

 
# Ramp the camera - these frames will be discarded and are only used to allow v4l2
# to adjust light levels, if necessary
for i in range(ramp_frames):
    temp = get_image()
    print("Taking image...")
    index=random.randint(1,1000)
    camera_capture = get_image()
    file = paths + "\\file" +str(index) +".jpg" #"C:\\Users\\Sujay022199\\.spyder-py3\\test5.jpg"

# Take the actual image we want to keep
# A nice feature of the imwrite method is that it will automatically choose the
# correct format based on the file extension you provide. Convenient!
    cv2.imwrite(file, camera_capture)
 
# You'll want to release the camera, otherwise you won't be able to create a new
# capture object until your script exits
#del(camera)