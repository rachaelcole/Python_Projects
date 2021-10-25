import socket

target_host = 'www.google.com'
target_port = 80

# Create a socket object; AF_INET indicates IPv4, and SOCK_STREAM indicates a TCP stream
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect the client
client.connect((target_host, target_port))
# Send some data as bytes
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
# Receive some data and print out the response
response = client.recv(4096)
print(response)
