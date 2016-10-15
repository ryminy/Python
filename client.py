import socket
import sys
import packet

val = ' '

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print( 'connecting to %s port %s' % server_address)
sock.connect(server_address)


passwd = input("PASSWORD: ") 

print(passwd)

#first send passwd
sock.sendall(passwd)
#2nd wait for OK/NK
data = sock.recv(2)
if data.decode() is 'OK':
    print("Connected to server!!")
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
   
