import socket

target_host = '127.0.0.1'
target_port = 9997

# Create socket object; AF_INET indicates we're using IPv4; SOCK_DGRAM indicates UDP datagrams
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Send some data as bytes
client.sendto(b"AAABBBCCC", (target_host, target_port))
# Receive some data and print it
data, addr = client.recvfrom(4096)
print(data)

# n.b. no need to call connect() method, because UDP is connectionless
