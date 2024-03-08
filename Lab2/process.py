'''
Author: Nabeel Ahmad
KUID: 3096518
Date: 02/05/2023
Lab: lab2
Last modified: 02/08/2023
Purpose: Contains a Process class. Handles the File I/O. Performs all of the functions for simulating the computer process. 
'''

#process.py

from stack import Stack

from function import Function

#makes a Process class
class Process:

    #initializes filename
    def __init__(self, filename):
        self.stack = Stack()

        self.filename = filename

        inputFile = open(filename, "r")

        self.inputList = []

        for line in inputFile:
            words = line.split()

            self.inputList.append(words)
    
    #prints a message to the screen indicating which process was created
    def start(self):
        for input in self.inputList:
            if input[0] == "START":
                self.stack.push(input[1])
    
        print(f"{self.stack.peek()} started")

    #prints a message to the screen indicating which process called the function and what the name of the function is
    def call(self):
        self.callCount = 0
        
        for input in self.inputList:
            if input[0] == "CALL":
                self.stack.push(input[1])

                print(f"{self.inputList[0][1]} calls {self.stack.peek()}")

                self.callCount += 1
        
    #if its main returns, the process ends. If a process ends, it displays a message indicating this
    def returnFunction(self):
        self.returnFunctionCount = 0

        for input in self.inputList:
            if input[0] == "RETURN":
                if self.returnFunctionCount == self.callCount:
                    print(f"{self.inputList[0][1]} has main return")

                    print(f"{self.inputList[0][1]} exited normally")

                    break
                
                else:
                    print(f"{self.inputList[0][1]} has {self.stack.pop()} return")
                    
                    self.returnFunctionCount += 1

    #Continue popping functions until a function is reached that handles the exception, or main is popped off, ending the process
    def raiseFunction(self):
        self.exceptionList = []
        
        for input in self.inputList:
            if input[0] == "CALL":
                if input[2] == "yes":
                    self.exceptionList.append(Function(input[1], True))

                elif input [2] == "no":
                    self.exceptionList.append(Function(input[1], False))

        for input in self.inputList:
            if input[0] == "RAISE":
                print(f"{self.inputList[0][1]} encountered a raised exception by: {self.stack.peek()}")
                
                reverseList = reversed(self.exceptionList)

                for answer in reverseList:
                    makeString = str(answer)

                    answerList = makeString.split(", ")

                    if answerList[0] == "True":
                        print(f"{self.inputList[0][1]} has exception handled by: {answerList[1]}")

                    elif answerList[0] == "False":
                        print(f"{self.inputList[0][1]} ends {answerList[1]} due to unhandled exception")
    
    #runs all of the previous functions
    def run(self):
        self.start()

        self.call()

        self.returnFunction()

        self.raiseFunction()
