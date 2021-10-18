import threading
import time

''' 
The threading module includes a locking mechanism to synchronise threads. A new lock is created by calling the lock()
method, which returns the new lock.
The acquire(blocking) method of the new lock object is used to force threads to run synchronously. The optional
blocking parameter lets you control whether the thread waits to acquire the lock.
If blocking=0, the thread returns immediately with a 0 value if the lock cannot be acquired and a 1 value if the lock
was acquired.
If blocking=1, the thread blocks and waits for the lock to be released.
The release() method is ued to release the lock when it is no longer required.
'''


class myThread(threading.Thread):

    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print(f'Starting {self.name}')
        # Get lock to synchronise threads
        threadLock.acquire()
        print_time(self.name, self.counter, 3)
        # Free lock to release to next thread
        threadLock.release()


def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print(threadName, time.ctime(time.time()))
        counter -= 1


threadLock = threading.Lock()
threads = []

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# Start new threads
thread1.start()
thread2.start()

# Add threads to thread list
threads.append(thread1)
threads.append(thread2)

# Wait for all threads to complete
for t in threads:
    t.join()
print('Exiting main thread')
