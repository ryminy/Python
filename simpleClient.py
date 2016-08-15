#!/usr/bin/env python

"""
An echo client that allows the user to send a char to the server.
Entering 'x' will exit the client.
"""

import socket
import sys

host = 'localhost'
port = 10000
size = 1

val = ' '
while True:
    try:

      # read from keyboard
      val = input("please enter a char:")
      if val == 'x':
       break
     
      if val < '0':
       break
      
      if val > 'z':
       break
     
      print("connection to server")
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((host,port))
      
      s.send(val.encode())
      
      print("receiving from server")
      data = s.recv(1)
      s.close()

      print(data.decode())
      
	
    except KeyboardInterrupt:
     print("silently dying")
     break

s.close() 
