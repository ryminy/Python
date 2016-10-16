import commands
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
      val = commands.encodeCommand()
      #Val = input("please enter a char:")
      if val == -1:
       print('invalid input');
       print('EXITING!')
       break
      else:
       print('Command is:' + str(val))

     
      print("connection to server")
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((host,port))
      
      s.send(chr(val).encode())
      
      data = s.recv(1)
      s.close()
      print("received from server:" + str(ord(data.decode())))      
	
    except KeyboardInterrupt:
     print("silently dying")
     break
    
try:
    s.close()
except:
    print('Caught an exception while closing')
