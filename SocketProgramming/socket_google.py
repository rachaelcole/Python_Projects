# An example script to connect to Google using socket programming in Python
# Referenced from geeksforgeeks.org
import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # creates a client socket
    print('Socket created successfully.')
except socket.error as err:
    print(f'Socket creation failed with error {err}.')   # error handling

port = 80  # set default port for socket (http)

try:
    host_ip = socket.gethostbyname('www.google.com')
except socket.gaierror:
    # this means could not resolve the host
    print('There was an error resolving the host.')
    sys.exit()

s.connect((host_ip, port))  # connecting to the server described as a tuple (hostname, port)

print(f'The socket has successfully connected to Google {host_ip} on port {port}.')
