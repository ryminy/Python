import socket
import sys
import packet

from packet import packetSend

OK  = '1'
NOK = '0'
passwd = 'ana'
msgLen = 3

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Bind the socket to the port
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(10)

while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    try:
        print >>sys.stderr, 'connection from', client_address

        # Receive the data in small chunks and retransmit it
        while True:

            #first wait for password
            data = connection.recv(len(passwd))
	    
            if data == passwd:
	        print >>sys.stderr, 'AUTHENTICATION PASSED', client_address
                connection.sendall(OK)
                
                #read messages
                data = connection.recv(msgLen)
                print >>sys.stderr, 'received "%s"' % data
                if data:
                    msgData = data[:2]
                    msgType = data[-1:]
                    
                    output = packetSend(msgData,msgType)
                    print >>sys.stderr, 'sending data back to the client'
                    connection.sendall(output[:3])
                    
		    break
	      
                else:
                    print >>sys.stderr, 'no more data from', client_address
                    break
            else:
	        print >>sys.stderr, 'AUTHENTICATION FAILED', client_address
                connection.sendall(NOK)
                break;
            
    finally:
        # Clean up the connection
	print >>sys.stderr, 'Connection closed with', client_address
        connection.close()
        
