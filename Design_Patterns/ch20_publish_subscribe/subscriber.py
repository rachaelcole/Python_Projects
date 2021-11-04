from re import S
from xmlrpc.client import ServerProxy
from xmlrpc.server import SimpleXMLRPCServer

class Subscriber(SimpleXMLRPCServer):
    def __init__(self, dispatcher, topic):
        super(Subscriber, self).__init__(('localhost', 9001))
        print('Listening on port 9001...')
        self.register_function(self.process, 'process')
        self.subscribe(dispatcher, topic)
    
    def subscribe(self, dispatcher, topic):
        with ServerProxy(dispatcher) as dispatch:
            dispatch.subscribe('http://localhost:9001', topic)
    
    def process(self, message):
        print(f"Message: {message.get('payload', 'DefaultMessage')}")
        return 'OK'

def main():
    subscriber_server = Subscriber('http://localhost:9000', 'MessageTopic')
    subscriber_server.serve_forever









# Reference: 
# Badenhurst, Wessel. "Chapter 20: Publish-Subscribe Pattern". Practical Python Design Patterns: Pythonic Solutions to Common Problems, Apress, October 20, 2017, pp. 315-326,
# DOI: https://doi.org/10.1007/978-1-4842-2680-3_20.