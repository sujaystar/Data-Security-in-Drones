# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 07:37:16 2019

@author: Sujay022199
"""

import socket                   # Import socket module

s = socket.socket()             # Create a socket object
#host = "1somehing.11somehing."  #Ip address that the TCPServer  is there
#port = 50000                     # Reserve a port for your service every new transfer wants a new port or you must wait.
host = socket.gethostname() # Get local machine name
port = 50000                # Reserve a port for your service.

s.connect((host, port))
#s.connect((host, port))
s.send('Hello server!'.encode())

with open('received_file', 'wb') as f:
    print('file opened')
    while True:
        print('receiving data...')
        data = s.recv(1024)
        print('data=%s', (data))
        f.write((data))
        if not data:
            break
        # write data to a file
        #f.write(data.decode())

f.close()
print('Successfully get the file')
s.close()
print('connection closed')