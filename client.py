import socket
import sys

OK = '1'

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

print("Connected to server!!")
passwd = raw_input("PASSWORD: ") 

print(passwd)

try:

    #first send passwd
    sock.sendall(passwd)

    # Look for the response
    amount_received = 0
    amount_expected = 1
    
    while amount_received < amount_expected:
        data = sock.recv(1)
        amount_received = len(data)

    if data == OK: 
            # Send data
            message = '0123456789012345'
            print >>sys.stderr, 'sending "%s"' % message
            sock.sendall(message)
            # Look for the response
            amount_received = 0
            amount_expected = len(message)

            while amount_received < amount_expected:
                data = sock.recv(len(message))
                amount_received += len(data)
                print >>sys.stderr, 'received "%s"' % data
    else:
        print("AUTHENTICATION FAILED")

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
