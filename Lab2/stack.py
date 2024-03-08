'''
Author: Nabeel Ahmad
KUID: 3096518
Date: 02/07/2023
Lab: lab2
Last modified: 02/07/2023
Purpose: Creates a Stack class and all of the supporting methods.
'''

#stack.py

from node import Node

#makes a Stack class
class Stack:

    #initializes self
    def __init__(self):
        self.top = None

    #puts the entry at the top of the Stack
    def push(self, entry):
        currentNode = self.top

        self.top = Node(entry)

        self.top.next = currentNode

    #Remove and returns the value at the top of the stack. Raises RuntimeError otherwise
    def pop(self):
        if self.top == None:
            raise RuntimeError("Pop attempted on an empty stack")
        
        else:
            currentTop = self.top.entry

            self.top = self.top.next

            return currentTop

    #Returns value at the top of the Stack. Raises a RuntimeError otherwise.
    def peek(self):
        if self.is_empty():
            raise Exception

        else:
            return self.top.entry

    #Returns True if Stack is empty. False otherwise
    def is_empty(self):
        if self.top == None:
            return True

        else:
            return False
