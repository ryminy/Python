import socket
import sys
import time
import Arduino

    
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print('starting up on ', server_address)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(10)

ser = Arduino.openSerial()
if( ser == 'X'):
    exit


while True:
    try:
      # Wait for a connection
      print('waiting for a connection')
      connection, client_address = sock.accept()
      
      print('connection from ', client_address)

      data = connection.recv(1)
      print('received from client:' + str(ord(data.decode())))
      Arduino.writeSerial(ser,data)
      time.sleep(.2)

      out = Arduino.readSerial(ser)
      
      if (out.decode().strip() == "R"):
          out = Arduino.readSerial(ser)
          
      print('sending data back to the client:' + str(ord(out.decode().strip())))

      connection.send(out)
	      
      # Clean up the connection
      print('Connection closed with', client_address)
      connection.close()
    
    except KeyboardInterrupt:
      print("silently dying")
      break

try:    
    Arduino.closeSerial(ser)
    connection.close()
    sock.close()
except:
    print('Caught an exception while exiting')
