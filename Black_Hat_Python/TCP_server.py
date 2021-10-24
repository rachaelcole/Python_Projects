import socket
import threading

bind_ip = '0.0.0.0'
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))  # Pass the IP and port we want the server to listen on
server.listen(5)  # Max backlog of connections set to 5
print(f'[*] Listening on {bind_ip}:{bind_port}')

# This is our client-handling thread
def handle_client(client_socket):
    # Print out what the client sends
    request = client_socket.recv(1024)
    print(f'[*] Received: {request}')
    # Send back a packet
    client_socket.send(b"ACK!")
    client_socket.close()

while True:
    client, addr = server.accept()
    print(f'[*] Accepted connection from {addr[0]:addr[1}')
    # Spin up our client thread to handle incoming data
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
