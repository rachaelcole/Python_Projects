import sys
import socket
import threading

HEX_FILTER = ''.join([(len(repr(chr(i))) == 3) and chr(i) or '.' for i in range(256)])  # List comprehension: for each
# int in range 0-2555, if length of the char = 3, we get the char, otherwise a dot


def hexdump(src, length=16, show=True):
    """Display the communication between the local and remote machines to the console."""
    if isinstance(src, bytes):  # Take some input as bytes or a string
        src = src.decode()  # Decode the bytes if bytes were passed
    results = list()

    for i in range(0, len(src), length):
        word = str(src[i:i+length]) # grab a piece of the string to dump and put it in the word variable
        printable = word.translate(HEX_FILTER)  # Substitute the string representation for the char in the raw string
        hexa = ' '.join([f'{ord(c):02X}' for c in word])  # List comprehension
        hexWidth = length * 3
        results.append(f'{i:04x}   {hexa:<{hexWidth}} {printable}')  # Create new array to hold the strings

    if show:
        for line in results:
            print(line)  # Print hexdump to console
        else:
            return results  # Return hexdump


def receive_from(connection):  # Pass in the socket object we want to use as 'connection'
    """Receive data from an incoming socket from either the local or remote machine."""
    buffer = b''  # Create an empty byte string that will accumulate responses from the socket
    connection.settimeout(5)  # Set a 5-second time-out by default (increase as necessary)

    try:
        while True:
            data = connection.recv(4096)  # Read response data into the buffer until no more data or timeout
            if not data:
                break
            buffer += data
    except Exception as e:
        pass

    return buffer  # Return the buffer byte string to the caller


def request_handler(buffer):
    """Modify request packets before sending them."""
    # Perform packet modifications, e.g., fuzzing, test for authentication issues, etc.
    return buffer


def response_handler(buffer):
    """Modify response packets before sending them."""
    # Perform packet modifications
    return buffer


def proxy_handler(client_socket, remote_host, remote_port, receive_first):
    """Manage the traffic direction between remote and local machines."""
    remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    remote_socket.connect((remote_host, remote_port))  # Connect to the remote host

    if receive_first:  # Check we don't need to initiate a connection to remote side and request data before main loop
        remote_buffer = receive_from(remote_socket)
        hexdump(remote_buffer)
    remote_buffer = response_handler(remote_buffer)  # Hand output response to response_handler() function

    if len(remote_buffer):
        print(f"[<==] Sending {len(remote_buffer)} bytes to localhost.")
        client_socket.send(remote_buffer)

    while True:
        # We set up this loop to continually read from local client, process data, send to remote client, read from
        # remote client, process data, and send to local client
        local_buffer = receive_from(client_socket)

        if len(local_buffer):
            line = f"[==>] Received {len(local_buffer)} bytes from localhost."
            print(line)
            hexdump(local_buffer)
            local_buffer = request_handler(local_buffer)
            remote_socket.send(local_buffer)
            print("[==>] Sent to remote.")
        remote_buffer = receive_from(remote_socket)

        if len(remote_buffer):
            print(f"[<==] Received {len(remote_buffer)} bytes from remote.")
            hexdump(remote_buffer)
            remote_buffer = response_handler(remote_buffer)
            client_socket.send(remote_buffer)
            print(f"[==>] Sent to localhost.")

        if not len(local_buffer) or not len(remote_buffer):  # When no more data, close the connection
            client_socket.close()
            remote_socket.close()
            print("[*] No more data. Closing connections.")
            break


def server_loop(local_host, local_port, remote_host, remote_port, receive_first):
    """Set up a listening socket and pass it to proxy_handler."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a socket

    try:
        server.bind((local_host, local_port))  # Bind to local host
    except Exception as e:
        print(f"Problem on bind: {e}")
        print(f"[!!] Failed to listen on {local_host}:{local_port}")
        print("[!!] Check for other listening sockets or correct permissions.")
        sys.exit(0)

    print(f"[*] Listening on {local_host}:{local_port}")
    server.listen(5)  # Start listening

    while True:  # Main loop: when a fresh connection request comes in, hand to proxy_handler in new thread
        client_socket, addr = server.accept()
        # Print out the local connection information
        line = f"> Received incoming connection from {addr[0]}:{addr[1]}"
        print(line)
        # Start a thread to talk to the remote host
        proxy_thread = threading.Thread(target=proxy_handler, args=(client_socket, remote_host, remote_port,
                                                                    receive_first))
        proxy_thread.start()


def main():
    # Check for correct command line input
    if len(sys.argv[1:]) != 5:
        print('Usage: ./proxy.py [localhost] [localport]', end='')
        print('[remotehost] [remoteport] [receive_first]')
        print('Example: ./proxy.py 127.0.0.1 9000 10.12.132.1 9000 True')
        sys.exit(0)
    # Set vars from command line args
    local_host = sys.argv[1]
    local_port = int(sys.argv[2])
    remote_host = sys.argv[3]
    remote_port = int(sys.argv[4])
    receive_first = sys.argv[5]
    if "True" in receive_first:
        receive_first = True
    else:
        receive_first = False
    # Call server loop function on above variables
    server_loop(local_host, local_port, remote_host, remote_port, receive_first)


if __name__ == '__main__':
    main()
