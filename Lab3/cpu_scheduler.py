'''
Author: Nabeel Ahmad
KUID: 3096518
Date: 02/14/2023
Lab: lab3
Last modified: 02/15/2023
Purpose: Handles File I/O. Performs methods that deal with what to do with each command from the input file.
'''

#cpu_scheduler.py

from process import Process

from linkedqueue import LinkedQueue

from stack import Stack

#makes a CPU_Scheduler class
class CPU_Scheduler:

    #initializes file handling
    def __init__(self, filename):
        self.linkedqueue = LinkedQueue()

        self.filename = filename

        inputFile = open(self.filename, "r")

        self.inputList = []

        for line in inputFile:
            words = line.split()

            self.inputList.append(words)

    #run the processes in the queue and handle "START", "CALL", "RETURN", and "RAISE" accordingly
    def execute(self):
        for command in self.inputList:
            if command[0] == "START":
                self.entry = Process(command[1])

                print(f"{self.entry.name} added to queue")

                self.linkedqueue.enqueue(self.entry)

            if command[0] == "CALL":
                self.front = self.linkedqueue.peek_front()

                self.front.callFunction(command[1], command[2])

                self.linkedqueue.dequeue()

                self.linkedqueue.enqueue(self.front)

            elif command[0] == "RETURN":
                self.front = self.linkedqueue.peek_front()

                self.front.returnFunction()

                self.linkedqueue.dequeue()

                if self.front.stack.is_empty() == False:
                    self.linkedqueue.enqueue(self.front)

                else:
                    print(f"{self.front.name} process has ended")

            elif command[0] == "RAISE":
                self.front = self.linkedqueue.peek_front()

                self.front.raiseFunction()

                self.linkedqueue.dequeue()

                self.linkedqueue.enqueue(self.front)

    #run the function
    def run(self):
        self.execute()