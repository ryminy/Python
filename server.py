import socket
import sys

OK  = '1'
NOK = '0'
passwd = 'ana'


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

            print data
            print passwd

            if data == passwd:
                connection.sendall(OK)
                
                #read messages
                data = connection.recv(16)
                print >>sys.stderr, 'received "%s"' % data
                if data:
                    print >>sys.stderr, 'sending data back to the client'
                    connection.sendall(data)
                else:
                    print >>sys.stderr, 'no more data from', client_address
                    break
            else:
                print("AUTHENTICATION FAILED")
                connection.sendall(NOK)

                break;
            
    finally:
        # Clean up the connection
        connection.close()
        
