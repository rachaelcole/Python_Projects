import socket
import threading

# Choosing nickname
nickname = input('Choose your nickname: ')

# Connecting to server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))

# Listening to server and sending nickname
def receive():
    while True:
        try:
            # Receive message from server
            # If 'NICK' send nickname
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            # Close connection when error
            print('An error occurred!')
            client.close()
            break

# Sending message to server
def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('ascii'))

# Starting threads for listening and writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()
write_thread = threading.Thread(target=write)
write_thread.start()

