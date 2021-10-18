import socket
import threading
from queue import Queue

# Define global variables
target = '127.0.0.1'  # localhost
queue = Queue()
open_ports = []

# Define port scan function
def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False

# Define function to get the ports we want to scan
def get_ports(mode):
    if mode == 1:
        for port in range(1, 1024):  # well-known ports
            queue.put(port)
    elif mode == 2:
        for port in range(1, 49152):  # include reserved ports
            queue.put(port)
    elif mode == 3:
        ports = [20, 21, 22, 23, 25, 53, 80, 110, 443]  # focus on these ports
        for port in ports:
            queue.put(port)
    elif mode == 4:
        ports = input("Enter your ports (separated by a space): ")  # user chooses which ports to scan
        ports = ports.split()
        ports = list(map(int, ports))
        for port in ports:
            queue.put(port)

# define a worker function for threads
def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print(f'Port {port} is open!')
            open_ports.append(port)


# define the main function that creates, starts, and manages threads
def run_scanner(threads, mode):
    get_ports(mode)
    thread_list = []
    for t in range(threads):
        thread = threading.Thread(target=worker)
        thread_list.append(thread)
    for thread in thread_list:
        thread.start()
    for thread in thread_list:
        thread.join()
    print(f'Open ports are: {open_ports}')


run_scanner(100, 1)
