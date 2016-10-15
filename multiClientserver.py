#!/usr/bin/env python

"""
An echo server that uses select to handle multiple clients at a time.
Entering any line of input at the terminal will exit the server.
"""

import select
import socket
import sys

from packet import packetSendAndReceive

host = 'localhost'
port = 10000
backlog = 5
size = 1

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen(backlog)
input = [server,sys.stdin]
running = 1
while running:
    try:
        inputready,outputready,exceptready = select.select(input,[],[])

        for connection in inputready:

            if connection == server:
                # handle the server socket
                client, address = server.accept()
                input.append(client)

            elif connection == sys.stdin:
                # handle standard input
                junk = sys.stdin.readline()
                running = 0

            else:
                # handle all other sockets
                print('connection from ', client)
                data = connection.recv(size)
                print('data received from client: ' + data.decode())
                output = packetSendAndReceive(data)
                print('sending data back to the client: ' + output)
                connection.send(output)
                print('Connection closed with', address)
                connection.close()
                input.remove(connection)
                
    except KeyboardInterrupt:
        print("silently dying")
        break

server.close() 
