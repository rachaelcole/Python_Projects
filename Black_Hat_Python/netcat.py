import argparse
import socket
import shlex
import sys
import textwrap
import threading
import subprocess


def execute(command):
    # Trim the newline
    command = command.strip()
    if not command:
        return
    # Run the command and get the output back
    output = subprocess.check_output(shlex.split(command), stderr=subprocess.STDOUT)  # Run the command we pass in
    # Send the output back to the client
    return output.decode()


class NetCat:
    def __init__(self, args, buffer=None):  # Initialise the NetCat object with:
        self.args = args  # the args from command line
        self.buffer = buffer  # the buffer
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # the socket object
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def run(self):
        if self.args.listen:
            self.listen()  # If we're setting up a listener
        else:
            self.send()  # Otherwise, call the send() method

    def send(self):
        self.socket.connect((self.args.target, self.args.port))  # Connect to the target and port
        if self.buffer:
            self.socket.send(self.buffer)  # If we have a buffer, send that to the target
        try:  # Set up a try/except block so we can manually close the connection with Ctrl-C
            while True:  # Start a loop to receive data from the target
                recv_len = 1
                response = ''
                while recv_len:
                    data = self.socket.recv(4096)
                    recv_len = len(data)
                    response += data.decode()
                    if recv_len < 4096:
                        break  # If there is no more data, break out of the loop
                if response:
                    print(response)
                    buffer = input('> ')
                    buffer += '\n'
                    self.socket.send(buffer.encode())  # Send the user's input
        except KeyboardInterrupt:      # The loop will continue until the keyboard interrupt (CTRL-C) occurs, which will
            print('User terminated.')  # close the socket
            self.socket.close()
            sys.exit()

    def listen(self):
        # Run the program as a listener
        self.socket.bind((self.args.target, self.args.port))  # Bind to the target and port
        self.socket.listen(5)
        while True:  # Start a listening loop
            client_socket, _ = self.socket.accept()
            client_thread = threading.Thread(target=self.handle, args=(client_socket, ))  # Pass the connected socket
            client_thread.start()                                                         # to the handle method

    def handle(self, client_socket):
        if self.args.execute:  # If a command should be executed the handle method passes that command to an execute
            output = execute(self.args.execute)  # function and sends the output back on the socket
            client_socket.send(output.encode())
        elif self.args.upload:  # Set up loop to listen for content and receive data
            file_buffer = b''
            while True:
                data = client_socket.recv(4096)
                if data:
                    file_buffer += data
                else:
                    break
            with open(self.args.upload, 'wb') as f:
                f.write(file_buffer)
            message = f'Saved file {self.args.upload}'
            client_socket.send(message.encode())
        elif self.args.command:  # If a shell to be created, set up a loop, prompt sender, and wait for user input
            cmd_buffer  = b''
            while True:
                try:
                    client_socket.send(b'BHP: #> ')
                    while '\n' not in cmd_buffer.decode():
                        cmd_buffer += client_socket.recv(64)
                    response = execute(cmd_buffer.decode())  # Execute the command using the execute function
                    if response:
                        client_socket.send(response.encode())
                    cmd_buffer = b''
                except Exception as e:
                    print(f'Server killed: {e}')
                    self.socket.close()
                    sys.exit()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='BHP Net Tool',  # Create a command line interface
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog=textwrap.dedent('''Example:   
netcat.py -t 192.168.1.108 -p 5555 -l -c  # Command shell
netcat.py -t 192.168.1.108 -p 5555 -l -u=mytest.txt  # Upload to file
netcat.py -t 192.168.1.108 -p 5555 -l -e=\\"cat/etc/passwd\\"  # Execute command
echo 'ABC' | ./netcat.py -t 192.168.1.108 -p 135  # echo text to server port 135
netcat.py -t 192.168.1.108 -p 5555  # Connect to server\n\n'''))
    parser.add_argument('-c', '--command', action='store_true', help='command shell')  # Add args that specify how we
    parser.add_argument('-e', '--execute', help='execute specified command')            # want the program to behave
    parser.add_argument('-l', '--listen', action='store_true', help='listen')
    parser.add_argument('-p', '--port', type=int, default=5555, help='specified port')
    parser.add_argument('-t', '--target', default='192.168.1.203', help='specified IP')
    parser.add_argument('-u', '--upload', help='upload file')
    args = parser.parse_args()
    if args.listen:  # if setting up a listener, invoke NetCat object with an empty buffer string
        buffer = ''
    else:  # otherwise, send the buffer content from stdin
        buffer = sys.stdin.read()
    nc = NetCat(args, buffer.encode())
    nc.run()
