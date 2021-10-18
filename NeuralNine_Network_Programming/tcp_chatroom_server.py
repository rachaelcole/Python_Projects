import socket
import threading

# Connection data
host = '127.0.0.1'
port = 55555

# Starting server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# List for clients and their nicknames
clients = []
nicknames = []

# Sending messages to all connected clients
def broadcast(message):
    for client in clients:
        client.send(message)

# Handling messages from clients
def handle(client):
    while True:
        try:
            # Broadcasting messages
            message = client.recv(1024)
            broadcast(message)
        except:
            # Removing and closing clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat'.encode('ascii'))
            nicknames.remove(nickname)
            break

# Receiving / listening function
def receive():
    while True:
        # Accept connection
        client, address = server.accept()
        print(f'Connected with {str(address)}')

        # Request and store nickname
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        # Print and broadcast nickname
        print(f'Nickname is {nickname}')
        broadcast(f'{nickname} joined the chat!'.encode('ascii'))
        client.send('Connected to server!'.encode('ascii'))

        # Start handling thread for client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

# Execute the receive() function to start the server
receive()
