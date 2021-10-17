# Server part of a simple server-client program
import socket

s = socket.socket()  # Creates a socket
print("Socket successfully created.")

# reserve a port on your computer
port = 12345

# bind to the port
s.bind(('', port))  # we have not typed an IP/hostname; an empty string makes the server listen for requests
print(f'Socket binded to {port}.')

# put socket into listening mode
s.listen(5)
print("Socket is listening.")

# a forever loop until we interrupt it or an error occurs:
while True:
    c, addr = s.accept()  # Establish connection with client
    print('Got connection from', addr)
    c.send('Thank you for connecting'.encode())  # sends thank you msg to client, encoded in bytes
    c.close()  # closes the connection with the client
    break  # breaks out of loop once connection closed
