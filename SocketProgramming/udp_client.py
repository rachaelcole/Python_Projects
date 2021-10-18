import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # For UDP
udp_host = socket.gethostname()  # host IP
udp_port = 12345  # specify port to connect
msg = "Hello Python!".encode('ascii')
print('UDP target IP: ', udp_host)
print('UDP target port: ', udp_port)
sock.sendto(msg, (udp_host, udp_port))  # Sending message to UDP server
