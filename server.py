import socket
import sys
import packet

from packet import packetSendAndReceive

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print('starting up on ', server_address)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(10)

while True:
    try:
      # Wait for a connection
      print('waiting for a connection')
      connection, client_address = sock.accept()
      
      print('connection from ', client_address)

      # Receive the data in small chunks and retransmit it
      #read messages
      data = connection.recv(1)
      print(data.decode())
      output = packetSendAndReceive(data)
      
      print('sending data back to the client')
      connection.send(output)
	      
      # Clean up the connection
      print('Connection closed with', client_address)
      connection.close()
    
    except KeyboardInterrupt:
      print("silently dying")
      break
    
connection.close()
sock.close()

