# Client part of a simple server-client program
import socket

s = socket.socket()  # Creates a socket
port = 12345  # define the port on which you want to connect
s.connect(('127.0.0.1', port))  # connect to server on local computer
print(s.recv(1024).decode())  # receive data from server and decode to get string
s.close()  # close the connection
