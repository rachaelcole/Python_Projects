import socket

server = '127.0.0.1'
port = 8080
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server, port))
client.sendall(bytes('This is from the client', 'utf-8'))
while True:
    in_data = client.recv(1024)
    print('From server: ', in_data.decode())
    out_data = input()
    client.sendall(bytes(out_data, 'utf-8'))
    if out_data == 'bye':
        break
client.close()
