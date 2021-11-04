# An observer pattern that can take different parameters to different objects using callbacks
# Observable objects take a changed flag which is checked at timed intervals to see if the object has changed states

import time

class ConcreteObserver(object):
    def update(self, observed):
        print(f'Observing: {observed}')

class Observable(object):
    def __init__(self):
        self.callbacks = set()
        self.changed = False
    def register(self, callback):
        self.callbacks.add(callback)
    def unregister(self, callback):
        self.callbacks.discard(callback)
    def unregister_all(self):
        self.callbacks = set()
    def poll_for_change(self):
        if self.changed:
            self.update_all()
    def update_all(self):
        for callback in self.callbacks:
            callback(self)

def main():
    observed = Observable()
    observer1 = ConcreteObserver()

    observed.register(lambda x: observer1.update(x))

    while True:
        time.sleep(3)
        observed.poll_for_change()  # Check if object changed states

if __name__ == "__main__":
    main()


# Reference: 
# Badenhurst, Wessel. "Chapter 14: Observer Pattern". Practical Python Design Patterns: Pythonic Solutions to Common Problems, Apress, October 20, 2017, pp. 219-237,
# DOI: https://doi.org/10.1007/978-1-4842-2680-3_14.