import socket, threading

class ClientThread(threading.Thread):
    def __init__(self, client_address, client_socket):
        threading.Thread.__init__(self)
        self.csocket = client_socket
        print(f'New connection added: {client_address}')

    def run(self):
        print(f'Connection from: {client_address}')
        self.csocket.send(bytes('Hi, this is from server...', 'utf-8'))
        msg = ''
        while True:
            data = self.csocket.recv(2048)
            msg = data.decode()
            if msg == 'bye':
                break
            print('from client:', msg)
            self.csocket.send(bytes(msg, 'utf-8'))
        print('Client at', client_address, ' disconnected...')

localhost = '127.0.0.1'
port = 8080
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((localhost, port))
print('Server started')
print('Waiting for client request...')
while True:
    server.listen(1)
    client_socket, client_address = server.accept()
    newthread = ClientThread(client_address, client_socket)
    newthread.start()
