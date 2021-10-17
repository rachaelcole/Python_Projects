import socket
'''Socket Programming

References:
https://www.geeksforgeeks.org/socket-programming-python/
https://www.tutorialspoint.com/python/python_networking.htm
https://realpython.com/python-sockets/
https://docs.python.org/3/howto/sockets.html


Sockets are used to send messages between nodes on a network. Client-side applications use client sockets only.
Servers use server sockets and client sockets. IPv4 TCP stream sockets are the most commonly used.
'''

# CLIENT-SIDE SOCKET
# create an Ipv4 streaming TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to web server on port 80 (http)
s.connect(('www.python.org', 80))  # socket connects to a tuple ('fqdn', port number)
# now that s is connected, it can send a request for a page, and then it is destroyed

# find an IP address using python
ip = socket.gethostbyname('www.google.com')
print(ip)



# SERVER-SIDE SOCKET
# create an IPv4 TCP streaming socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to a public host and a well-known port
serversocket.bind((socket.gethostname(), 80))
# become a server socket
serversocket.listen(5)  # this socket will take up to 5 connect requests

# sample main loop of a web server
while True:
    # accept connections from outside
    (clientsocket, address) = serversocket.accept()
    # now do something with the clientsocket - here we will pretend it is a threaded server
    ct = client_thread(clientsocket)
    ct.run()

'''
Primary socket API functions and methods are:
socket()    bind()      accept()    listen()
connect()   connect_ex()    send()  recv()
close()
The API calls the server makes to set up a 'listening socket' are socket(), bind(), listen(), and accept().
a listening socket listens for connections from clients
when a client connects, the server calls accept() to complete/accept the connection
the CLIENT calls connect() to initiate the TCP 3-way handshake
data is exchanged btwn client and server using calls to send() and recv()
when data transfer is complete, both client and server call close() to destroy their sockets
'''

'''
SAMPLE SERVER SOCKET CODE
'''
host = '127.0.0.1'  # Standard loopback IP address (localhost)
port = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  # Creates a socket object; using a with statement means we don't have to call s.close() later
    s.bind((host, port))  # Associate the socket object with a specific network interface and port number
    s.listen()  # Enables the server to accept() connections; makes the socket a 'listening' socket
    conn, addr = s.accept()  # Blocks and waits for an incoming connection; when client connects, it returns a NEW SOCKET OBJECT and a tuple (host, port) representing the client
    with conn:  # conn is the client socket object; infinite while loop used to loop over blocking calls to conn.recv()
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:  # if conn receives an empty byte object, the loop breaks, sockets die
                break
            conn.sendall(data)

'''
SAMPLE CLIENT SOCKET CODE
'''
host = '127.0.0.1'  # the server's hostname or IP address
port = 65432  # the port used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    s.sendall(b'Hello, world')
    data = s.recv(1024)  # reads the server's reply
print('Received', repr(data))  # prints the server's reply
