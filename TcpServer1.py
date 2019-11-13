# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 07:40:22 2019

@author: Sujay022199
"""

import socket                   # Import socket module
import os
import random
#port = 50000                    # Reserve a port for your service every new transfer wants a new port or you must wait.
s = socket.socket()             # Create a socket object
#host = ""   # Get local machine name
host = socket.gethostname() # Get local machine name
port = 50000
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.
files=os.listdir("C:\\Users\\Sujay022199\\.spyder-py3")
print('Server listening....')
for i in files:
    index=random.randint(1,1000)
    if i[0]=='b':
        fname="ebfile"+str(index)
    elif i[0]=='c':
        fname="ecfile"+str(index)
    else:
        fname="effile"+str(index)

    while True:
        conn, addr = s.accept()     # Establish connection with client.
        print ('Got connection from', addr)
        data = conn.recv(1024)
        print('Server received', repr(data))
    
   
    
        filename="C:\\Users\\Sujay022199\\.spyder-py3\\"+fname+".jpg"#'test6.jpg' #In the same folder or path is this file running must the file you want to tranfser to be
        f = open(filename,'rb')
        l = f.read(1024)#1024)
        print(l)
        while (l):
            conn.send(l)
            print('Sent ',repr(l))
            l = f.read(1024)
            f.close()

        print('Done sending')
        conn.send('Thank you for connecting'.encode())
        conn.close()