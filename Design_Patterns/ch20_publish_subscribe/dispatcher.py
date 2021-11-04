from xmlrpc import server
# Building a simple message sender using the publisher-subscriber pattern and XML-RPC

from xmlrpc.client import ServerProxy
from xmlrpc.server import SimpleXMLRPCServer

class Dispatcher(SimpleXMLRPCServer):
    def __init__(self):
        self.topic_subscribers = dict()
        super(Dispatcher, self).__init__(('localhost', 9000))
        print('Listening on port 9000...')
        self.register_function(self.subscribe, 'subscribe')
        self.register_function(self.unsubscribe, 'unsubscribe')
        self.register_function(self.unsubscribe_all, 'unsubscribe_all')
        self.register_function(self.send, 'send')
    
    def subscribe(self, subscriber, topic):
        print(f'Subscribing {subscriber} to {topic}')
        self.topic_subscribers.setdefault(topic, set()).add(subscriber)
        return 'OK'

    def unsubscribe(self, subscriber, topic):
        print(f'Unsubscribing {subscriber} from {topic}')
        self.topic_subscribers.setdefault(topic, set()).discard(subscriber)
        return 'OK'
    
    def unsubscribe_all(self, topic):
        print(f'Unsubscribing all from {topic}')
        self.subscribers = self.topic_subscribers[topic] = set()
        return 'OK'
    
    def send(self, message):
        print('Sending Message:\nTopic: {}\nPayload: {}'.format(message['topic'], message['payload']))
        for subscriber in self.topic_subscribers[message.get('topic', 'all')]:
            with ServerProxy(subscriber) as subscriber_proxy:
                subscriber_proxy.process(message)
        return 'OK'

def main():
    dispatch_server = Dispatcher()
    dispatch_server.serve_forever()

if __name__ == "__main__":
    main()






# Reference: 
# Badenhurst, Wessel. "Chapter 20: Publish-Subscribe Pattern". Practical Python Design Patterns: Pythonic Solutions to Common Problems, Apress, October 20, 2017, pp. 315-326,
# DOI: https://doi.org/10.1007/978-1-4842-2680-3_20.



# Reference: 
# Badenhurst, Wessel. "Chapter 20: Publish-Subscribe Pattern". Practical Python Design Patterns: Pythonic Solutions to Common Problems, Apress, October 20, 2017, pp. 315-326,
# DOI: https://doi.org/10.1007/978-1-4842-2680-3_20.