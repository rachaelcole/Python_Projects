import threading
import time

'''
MULTITHREADED SOCKET PROGRAMMING

Describes a Multithreaded Socket Server that can communicate with more than one client at the same time in the same
network.

Running several threads is similar to running different programs concurrently, but with the following benefits:
    - multiple threads within a process share the same data space with the main thread and can therefore share
      information or communicate with each other more easily than if they were separate processes
    - threads are sometimes called lightweight processes; they don't require much memory overhead and are cheaper
      than processes

A thread has a beginning, an execution sequence, and a conclusion. It has an instruction pointer that keeps track
of where within it context it is currently running: it can be pre-empted (interrupted) and temporarily put on
hold (sleeping) while other threads are running,  called yielding.
'''


# Creating a thread using the threading module
exit_flag = 0
# Define a new subclass of the Thread class
class myThread(threading.Thread):
    # Override the __init__(self[, args]) method to add additional arguments
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    # Override the run(self[, args]) to implement what the thread should do when started
    def run(self):
        print(f'Starting {self.name}')
        print_time(self.name, 5, self.counter)
        print(f'Exiting {self.name}')

def print_time(threadName, counter, delay):
    while counter:
        if exit_flag:
            threadName.exit()
        time.sleep(delay)
        print(threadName, time.ctime(time.time()))
        counter -= 1

# Create an instance of the new Thread subclass
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)
# Start a new thread by invoking the start() method
thread1.start()
thread2.start()

print('Exiting main thread')
