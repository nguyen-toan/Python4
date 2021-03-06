#!/bin/env python
# -*- coding: utf-8 -*-

class Publisher:  
    def __init__(self):
        "Create a dictionary to store each subscriber and its number of times the process() method has been called"
        self.subscribers = {}
    def subscribe(self, subscriber):
        "Add an subscriber and initialize its number of times which the process() method has been called to 0"
        if subscriber in self.subscribers:
            raise ValueError("Multiple subscriptions are not allowed")
        self.subscribers[subscriber] = 0
    def unsubscribe(self, unsubscribers):
        "Remove subscribers"
        self.subscribers = dict( (k,v) for k,v in self.subscribers.items() if k not in unsubscribers)
    def publish(self, s):
        unsubscribers = []
        for subscriber in self.subscribers:
            subscriber(s)
            self.subscribers[subscriber] += 1
            if self.subscribers[subscriber] == 3:
                unsubscribers.append(subscriber)
        "Remove subscribers (if any) which have processed three messages"
        if len(unsubscribers) > 0:
            self.unsubscribe(unsubscribers)

class SimpleSubscriber:
    def __init__(self, name, publisher):
        self.name = name
        self.publisher = publisher
        publisher.subscribe(self.process)
    def process(self, s):
        print(self.name, ":", s.upper())
    def __repr__(self):
        return self.name

def multiplier(s):
    print(2 * s)

if __name__ == '__main__':    
    publisher = Publisher()
    publisher.subscribe(multiplier)
    for i in range(6):
        newsub = SimpleSubscriber("Sub" + str(i), publisher)
        line = input("Input {}: ".format(i))
        publisher.publish(line)
