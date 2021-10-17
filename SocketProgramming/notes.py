import socket
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import poplib
from urllib import urlopen
import webbrowser
import ftplib

'''Socket Programming

References:
https://www.geeksforgeeks.org/socket-programming-python/
https://www.tutorialspoint.com/python/python_networking.htm
https://realpython.com/python-sockets/
https://docs.python.org/3/howto/sockets.html
http://net-informations.com/python/net/default.htm


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

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  # Creates a socket object; using a with statement
                                                              # means we don't have to call s.close() later
    s.bind((host, port))  # Associate the socket object with a specific network interface and port number
    s.listen()  # Enables the server to accept() connections; makes the socket a 'listening' socket
    conn, addr = s.accept()  # Blocks and waits for an incoming connection; when client connects,
                             # it returns a NEW SOCKET OBJECT and a tuple (host, port) representing the client
    with conn:  # conn is the client socket object; infinite while loop used to loop over blocking
                # calls to conn.recv()
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



'''
Python is an object-oriented programming language with a standard library that includes everything needed to 
rapidly build powerful network apps. Python lets us see the low-level networking commands available to the C 
languages, and also has modules that implement higher-level application-layer protocols. Python has libraries
that provide access to TCP, FTP, SMTP, HTTP, etc.
Sockets exist on the Transport layer (Layer 4). Sockets are uniquely identified by an IP address, a port
number, and a protocol. 
'''

# Find the hostname
hostname = socket.gethostname()
# OR
hostname2 = socket.gethostbyaddr(socket.gethostname())[0]

# Get the FQDN
host_fqdn = socket.getfqdn("209.191.88.254")

# Get network name
network_name = platform.node()

# Get username of a computer
my_host = os.uname()[1]
print(my_host)

# Get an IP address
ipv4 = socket.gethostbyname(socket.gethostname())

# Translate a host name to IPv4 address format
ipv4_format = socket.gethostbyname('www.google.com')

'''
MULTITHREADED SOCKET PROGRAMMING

Describes a Multithreaded Socket Server that can communicate with more than one client at the same time in the same
network.
'''

'''
OTHER NETWORK PROGRAMMING TOOLS AND MODULES

Sending email with Python is done using smtplib and an SMTP server. smtplib defines an SMTP client session object that
can send mail to any Internet machine with an SMTP/ESMTP listener daemon. MIME is an Internet standard that allows
more multimedia in emails (images, sound, text, etc.).
'''
# Sending email using SMTP server
fromaddr = "youraddress@gmail.com"
toaddr = "some_other_email@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Test Subject"
body = "Write your message here"
msg.attach(MIMEText(body, 'plain'))
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(fromaddr, "your_passw0rd")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

# Retrieving emails using POP3 server
pop3server = 'pop.gmail.com'
username = 'username@gmail.com'
password = 'y0ur_p@ssw0rd'
pop3server = poplib.POP3_SSL(pop3server)  # Open secure connection to POP3 server
print(pop3server.getwelcome())  # Show welcome message
pop3server.user(username)
pop3server.pass_(password)
pop3info = pop3server.stat()  # Access mailbox status
mailcount = pop3info[0]  # Total emails
print(f'Total number of emails is {mailcount}')
print(f'\n\nStart Reading Messages\n\n')
for i in range(mailcount):
    for message in pop3server.retr(i+1)[1]:
        print(message)
pop3server.quit()


# Get webpage contents via HTTP
html = urlopen('http://net-informations.com/about.htm')
print(html.read())

# Open a web browser
webbrowser.open('http://net-informations,co', new=2)  # if new=0, same window/tab; if new=1, new window
                                                      # if new=2, new tab

# connect to FTP server
ftpServer = ftplib.FTP('ftp.swfwmd.state.fl.us', 'anonymous', 'sample@email.com')
ftpServer.retrlines("LIST")
dirList = []
ftpServer.retrlines("LIST", dirList.append())
str = dirList[0].split(None, 8)
filename = str[-1].strip()
print("Downloading file: ", filename)
localPath = os.path.join(r"D:\ftp\downloads", filename)
file = open(localPath, "wb")
ftpServer.retrbinary("RETR " + filename, file.write(), 8*1024)
file.close()
print("Done!")
print(r"Please check your downloaded file: D:\ftp\downloads")
