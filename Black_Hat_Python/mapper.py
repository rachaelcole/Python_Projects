import contextlib
import os
import queue
import requests
import sys
import threading
import time

FILTERED = [".jpg", ".gif", ".png", ".css"]  # Filter these OUT
TARGET = "http://boodelyboo.com/wordpress"  # Target URL
THREADS = 10

answers = queue.Queue()
web_paths = queue.Queue()  # Where we'll store the files we'll attempt to locate on the remote server


def gather_paths():
    for root, _, files in os.walk('.'):  # Walk through all the files in the local web app directory
        for fname in files:
            if os.path.splitext(fname)[1] in FILTERED:
                continue
            path = os.path.join(root, fname)
            if path.startswith('.'):
                path = path[1:]
            print(path)
            web_paths.put(path)


def test_remote():
    while not web_paths.empty():  # Keeps executing until web_path's Queue is empty
        path = web_paths.get()  # Grab a path from the Queue
        url = f'{TARGET}{path}'  # Add it to the target website's base path
        time.sleep(2)  # compensate for throttling/lockout
        r = requests.get(url)
        if r.status_code == 200:  # If successful
            answers.put(url)  # Put the URL into the answers queue
            sys.stdout.write('+')
        else:
            sys.stdout.write('x')
        sys.stdout.flush()


@contextlib.contextmanager  # context manager with generator
def chdir(path):
    """On enter, change directory to specified path.
    On exit, change directory back to original."""
    this_dir = os.getcwd()
    os.chdir(path)
    try:
        yield  # Yield control back to gather_paths()
    finally:
        os.chdir(this_dir)  # Revert back to original directory


def run():
    mythreads = list()
    for i in range(THREADS):
        print(f'Spawning thread {i}')
        t = threading.Thread(target=test_remote)
        mythreads.append(t)
        t.start()
    for thread in mythreads:
        thread.join()

if __name__ == '__main__':
    with chdir("C:\\Users\\Rachael\\Downloads\\wordpress"):
        gather_paths()
    input("Press Enter to continue")
    run()
    with open('myanswers.txt', 'w') as f:
        while not answers.empty():
            f.write(f'{answers.get()}\n')
        print('Done')
