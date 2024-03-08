'''
Author: Nabeel Ahmad
KUID: 3096518
Date: 02/21/2023
Lab: lab4
Last modified: 02/21/2023
Purpose: Creates a Linked List class. Contains all of the associated methods
'''

#linkedlist.py

from node import Node

#creates a Linked List class
class LinkedList:

    #initializes list
    def __init__(self):
        self.front = None
    
    #return length of the list
    def lengthFunction(self):
        currentNode = self.front

        length = 0

        while currentNode != None:
            length += 1

            currentNode = currentNode.next
        
        return length

    #insert the entry at the front of the list
    def insertFront(self, entry):
        self.front = Node(entry, self.front)
    
    #insert the entry at the back of the list
    def insertBack(self, entry):
        if self.front == None:
            self.front = Node(entry, self.front)

        else:
            finalNode = self.front

            while True:
                if finalNode.next == None:
                    break

                finalNode = finalNode.next

            finalNode.next = Node(entry)
    
    #insert the entry at a specific index
    def insert(self, index, entry):
        if index < 0 or index > self.lengthFunction():
            print("Invalid index")
        
        if index == 0:
            self.insertFront(entry)
        
        currentNode = self.front

        currentIndex = 0

        while True:
            if currentIndex == index:
                previousNode.next = entry

                entry.next = currentNode

                break

            previousNode = currentNode

            currentNode = currentNode.next

            currentIndex += 1
    
    #removes the entry at the front of the list
    def removeFront(self):
        if self.lengthFunction() != 0:
            previousFront = self.front

            self.front = self.front.next

            previousFront.next = None

        else:
            print("Linked list is empty")

    #removes the entry at the back of the list
    def removeBack(self):
        if self.lengthFunction() != 0:
            if self.front.next == None:
                self.removeFront()
            
            finalNode = self.front

            while finalNode != None:
                previousNode = finalNode

                finalNode = finalNode.next

            previousNode.next = None

        else:
            print("Linked list is empty")

    #removes the entry at a specific index
    def remove(self, index):
        if index < 0 or index > self.lengthFunction():
            print("Invalid index")

            return

        if self.lengthFunction() > 0:
            if index == 0:
                self.removeFront()

                return

            currentNode = self.front

            currentIndex = 0

            while True:
                if currentIndex == index:
                    previousNode.next = currentNode.next

                    currentNode.next = None

                    break

                previousNode = currentNode

                currentNode = currentNode.next

                currentIndex += 1

        else:
            print("Linked list is empty")

    #return the entry at index, raises a RuntimeError otherwise
    def get_entry(self, index):
        if 0 <= index and index < self.lengthFunction():
            jumper = self.front

            for num in range(index):
                jumper = jumper.next

            return jumper.entry

        else:
            raise RuntimeError

    #sets the entry at index, raises a RuntimeError otherwise. Even if successful, the length remains the same
    def set_entry(self, index, entry):
        if 0 <= index and index < self.lengthFunction():
            jumper = self.front

            for num in range(index):
                jumper = jumper.next
            
            jumper.entry = entry
        
        else:
            raise RuntimeError

    #prints the list
    def printList(self):
        if self.front == None:
            print("The list is empty")

            return
        
        currentNode = self.front

        while True:
            if currentNode is None:
                break

            print(currentNode.entry)

            currentNode = currentNode.next

    #clears the list
    def clear(self):
        self.front = None

        self.lengthFunction = 0
