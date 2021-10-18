import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # for UDP
udp_host = socket.gethostname()  # Host IP
udp_port = 12345  # specify a port to connect
sock.bind((udp_host, udp_port))
while True:
    print('Waiting for client...')
    data, addr = sock.recvfrom(1024)  # Receive data from client
    print('Received messages: ', data, ' from', addr)
    
