# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 04:01:52 2019

@author: Sujay022199
"""
import time
start=time.time()
fo=open("test5.jpg","rb")
image=fo.read()
fo.close
image=bytearray(image)
key=48
for index,value in enumerate(image):
    image[index]=value^key
    
fo=open("test6.jpg","wb")
fo.write(image)
fo.close
end=time.time()
print(end-start)