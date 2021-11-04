# Publish-Subscriber pattern

# This pattern extends the observer pattern and allows us to decouple the observer from the observable even more. We will extend the one-to-
# many approach of the observer pattern to a many-to-many relationship between observables and observers, such that one class of objects 
# doesn't need to know much about the other. The blind observables are publishers, and the disconencted observers are subscribers.

class Message(object):
    def __init__(self):
        self.payload = None
        self.topic = 'all'


class Subscriber(object):
    def __init__(self, dispatcher, topic):
        dispatcher.subscribe(self, topic)

    def process(self, message):
        print(f'Message: {message.payload}')


class Publisher(object):
    def __init__(self, dispatcher):
        self.dispatcher = dispatcher
        
    def publish(self, message):
        self.dispatcher.send(message)

class Dispatcher(object):
    def __init__(self):
        self.topic_subscribers = dict()
     
    def subscribe(self, subscriber, topic):
        self.topic_subscribers.setdefault(topic, set()).add(subscriber)

    def unsubscribe(self, subscriber, topic):
        self.topic_subscribers.setdefault(topic, set()).discard(subscriber)
    
    def unsubscribe_all(self, topic):
        self.subscribers = self.topic_subscribers[topic] = set()
    
    def send(self, message):
        for subscriber in self.topic_subscribers[message.topic]:
            subscriber.process(message)


def main():
    dispatcher = Dispatcher()
    publisher_1 = Publisher(dispatcher)
    subscriber_1 = Subscriber(dispatcher, 'topic1')
    message = Message()
    message.payload = 'My payload'
    message.topic = 'topic1'
    publisher_1.publish(message)


if __name__ == "__main__":
    main()
    





# Reference: 
# Badenhurst, Wessel. "Chapter 20: Publish-Subscribe Pattern". Practical Python Design Patterns: Pythonic Solutions to Common Problems, Apress, October 20, 2017, pp. 315-326,
# DOI: https://doi.org/10.1007/978-1-4842-2680-3_20.