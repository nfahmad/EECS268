'''
Author: Nabeel Ahmad
KUID: 3096518
Date: 02/14/2023
Lab: lab3
Last modified: 02/15/2023
Purpose: Contains a Process class. Performs all of the methods for simulating the various processes. 
'''

#process.py

from stack import Stack

from function import Function

#makes a Process class
class Process:

    #initialization of class
    def __init__(self, name):
        self.stack = Stack()

        self.name = name

        self.stack.push(Function("main", "no"))
    
    #prints a message to the screen indicating which process was started
    def start(self):
        for input in self.inputList:
            if input[0] == "START":
                self.stack.push(input[1])
    
        print(f"{self.stack.peek()} started")

    #prints a message to the screen indicating which process called the function and what the name of the function is
    def callFunction(self, command, isValid):
        self.stack.push(Function(command, isValid))

        print(f"{self.name} calls {command}")
        
    #if the stack is empty, the process ends. If a process ends, it displays a message indicating this. Otherwise if the stack is not empty, it returns the top of the stack.
    def returnFunction(self):
        if self.stack.is_empty():
            print(f"{self.name} process has ended")

        else:
            print(f"{self.name} returns from {self.stack.pop().name}")

    #handle exceptions based on "yes" or "no"
    def raiseFunction(self):
        print(f"{self.name} encountered a raised exception by {self.stack.peek().name}")

        while True:
            if self.stack.is_empty():
                print(f"{self.name} ends due to unhandled exception")

                break

            elif self.stack.peek().exceptionHandling == "no":
                print(f"{self.name} ends {self.stack.pop().name} due to unhandled exception")

            elif self.stack.peek().exceptionHandling == "yes":
                print(f"{self.name} has exception handled by: {self.stack.pop().name}")

                break
