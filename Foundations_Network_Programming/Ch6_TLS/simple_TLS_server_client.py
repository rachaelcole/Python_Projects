# Simple TLS client and server

import argparse, socket, ssl

def client(host, port, cafile=None):
    purpose = ssl.Purpose.SERVER_AUTH
    # Create a TLS context object
    context = ssl.create_default_context(purpose, cafile=cafile)

    raw_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    raw_sock.connect((host, port))
    print(f'Connected to host {host} and port {port}')
    # Use the wrap_socket() method to let the OpenSSL library take control of the TCP connection
    ssl_sock = context.wrap_socket(raw_sock, server_hostname=host)
    while True:
        # Perform all further communication with the ssl_sock object
        data = ssl_sock.recv(1024)
        if not data:
            break
        print(repr(data))


def server(host, port, certfile, cafile=None):
    purpose = ssl.Purpose.CLIENT_AUTH
    context = ssl.create_default_context(purpose, cafile=cafile)
    context.load_cert_chain(certfile)

    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    listener.bind((host, port))
    listener.listen(1)
    print(f'Listening at interface {host} and port {port}')
    raw_sock, address = listener.accept()
    print(f'Connection from host {address} ')
    ssl_sock = context.wrap_socket(raw_sock, server_side=True)

    ssl_sock.sendall('Simple is better than complex'.encode('ascii'))
    ssl_sock.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Safe TLS client and server')
    parser.add_argument('host', help='hostname or IP address')
    parser.add_argument('port', type=int, help='TCP port number')
    parser.add_argument('-a', metavar='cafile', default=None, help='authority: path to CA certificate PEM file')
    parser.add_argument('-s', metavar='certfile', default=None, help='run as server: path to server PEM file')
    args = parser.parse_args()
    if args.s:
        server(args.host, args.port, args.s, args.a)
    else:
        client(args.host, args.port, args.a)
