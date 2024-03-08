'''
Author: Nabeel Ahmad
KUID: 3096518
Date: 04/25/2023
Lab: lab9
Last modified: 04/26/2023
Purpose: Handle file I/O.
'''

#executive.py

from maxheap import MaxHeap

from patienthandler import PatientHandler

#creates an Executive class
class Executive:

    #initialize the file and interact with the max heap based on commands
    def __init__(self, filename):
        inputFile = open(filename, "r")

        self.maxHeap = MaxHeap()

        for line in inputFile:
            commands = line.split()

            if commands[0] == "ARRIVE":
                self.maxHeap.add(PatientHandler(commands[1], commands[2], commands[3], commands[4], commands[5]))

            elif commands[0] == "NEXT":
                if self.maxHeap.count() == 0:
                    print("There are no patients left\n")
                
                else:
                    print("Next patient:")

                    self.maxHeap.printMaxHeap()

            elif commands[0] == "TREAT":
                self.maxHeap.remove()

            elif commands[0] == "COUNT":
                if self.maxHeap.count() == 1:
                    print("There is 1 patient waiting.\n")

                else:
                    print(f"There are {self.maxHeap.count()} patients waiting.\n")
            
            else:
                raise Exception("Invalid input")