# An observer pattern includes an Observable class, which can be watched by other classes, and an Observer class,
# which is alerted whenever an Observable object that the two classes are connected to undergoes a change. It is
# a design pattern where an object (the subject) maintains a list of dependents (obserbers) and notifies them of
# any state changes (usually by calling one of their methods). It is mainly used to implement distributed event
# handling systems (Gamme, E., Helm, R., Johnson, R., Vlissides, J. Design Patterns: Elements of Reusable Object-
# Oriented Software, Addison-Wesley, 1994).

# An observer pattern looks like this:

class ConcreteObserver(object):
    def update(self, observed):
        print(f'Observing: {observed}')


class Observable(object):
    """Keeps a record of all the objects observing it in 'observers'. When relevant changes
    happen in this object, it runs the update() method for each observer."""
    def __init__(self):
        self.observers = set()
    
    def register(self, observer):
        self.observers.add(observer)
    
    def unregister(self, observer):
        self.observers.discard(observer)
    
    def unregister_all(self):
        self.observers = set()
    
    def update_all(self):
        for observer in self.observers:
            observer.update(self)






# Reference: 
# Badenhurst, Wessel. "Chapter 14: Observer Pattern". Practical Python Design Patterns: Pythonic Solutions to Common Problems, Apress, October 20, 2017, pp. 219-237,
# DOI: https://doi.org/10.1007/978-1-4842-2680-3_14.