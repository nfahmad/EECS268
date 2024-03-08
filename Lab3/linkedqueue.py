'''
Author: Nabeel Ahmad
KUID: 3096518
Date: 02/14/2023
Lab: lab3
Last modified: 02/15/2023
Purpose: Creates a linkedqueue class and all of the supporting methods.
'''

#linkedqueue.py

from node import Node

#creates a linkedqueue class
class LinkedQueue:

    #initialization
    def __init__(self):
        self.front = None

        self.back = None
    
    #puts the entry at the back of the queue
    def enqueue(self, entry):
        newNode = Node(entry)

        if self.front == None:
            self.front = newNode

            self.back = self.front

        else:
            self.back.next = newNode

            self.back = newNode
    
    #removes and returns the value at the front of the queue. Raises RuntimeError otherwise
    def dequeue(self):
        if self.front == None:
            raise RuntimeError

        entry = self.front.entry

        self.front = self.front.next

        if self.front == None:
            self.back == None
        
        return entry

    #returns value at the front of the queue, raises a RuntimeError otherwise
    def peek_front(self):
        if self.is_empty():
            raise RuntimeError
        else:
            return self.front.entry

    #returns True if queue is empty, returns False otherwise
    def is_empty(self):
        if self.front == None:
            return True

        else:
            return False
            