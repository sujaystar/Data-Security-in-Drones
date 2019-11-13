# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 04:06:56 2019

@author: Sujay022199
"""
import time
start=time.time()
fo=open("received_file","rb")
image=fo.read()
print(image)
fo.close()
image=bytearray(image)
key=48
for index,value in enumerate(image):
    image[index]=value^key
    
fo=open("test7.jpg","wb")
fo.write(image)
fo.close
end=time.time()
print(end-start)