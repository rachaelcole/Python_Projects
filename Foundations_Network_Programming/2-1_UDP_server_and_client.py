import argparse, socket
from datetime import datetime

'''
N.b. this code is not secure at all - although recvfrom() returns the address of the incoming datagram, this code
never checks the source address of the datagram received to verify it is actually from the server!
'''

MAX_BYTES = 65535


def server(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1', port))
    print(f'Listening at {sock.getsockname()}...')
    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        text = data.decode('ascii')
        print(f'The client at {address} says {text}.')
        text = f'Your data was {len(data)} bytes long.'
        data = text.encode('ascii')
        sock.sendto(data, address)


def client(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    text = 'The time is'.format(datetime.now())
    data = text.encode('ascii')
    sock.sendto(data, ('127.0.0.1', port))
    print(f'The OS assigned me to the address {sock.getsockname()}')
    data, address = sock.recvfrom(MAX_BYTES)  # Danger!
    text = data.decode('ascii')
    print('The server {} replied {!r}'.format(address, text))


if __name__ == "__main__":
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='Send and receive UDP locally')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060, help='UDP port (default 1060)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.p)
