from xmlrpc.client import ServerProxy

class Publisher(object):
    def __init__(self, dispatcher):
        self.dispatcher = dispatcher
    def publish(self, message):
        with ServerProxy(self.dispatcher) as dispatch:
            dispatch.send(message)

def main():
    message = {'topic': 'MessageTopic', 'payload': 'This is an awesome payload'}
    publisher = Publisher('http://localhost:9000')
    publisher.publish(message)

if __name__ == "__main__":
    main()




# Reference: 
# Badenhurst, Wessel. "Chapter 20: Publish-Subscribe Pattern". Practical Python Design Patterns: Pythonic Solutions to Common Problems, Apress, October 20, 2017, pp. 315-326,
# DOI: https://doi.org/10.1007/978-1-4842-2680-3_20.