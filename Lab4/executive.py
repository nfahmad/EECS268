'''
Author: Nabeel Ahmad
KUID: 3096518
Date: 02/21/2023
Lab: lab4
Last modified: 02/21/2023
Purpose: Handle File I/O. Interact with the browser class based on commands from the input file
'''

#executive.py

from browser import Browser

#creates an Executive class
class Executive:

    #initialize the file and interact with the browser class based on commands
    def __init__(self, filename):
        inputFile = open(filename, "r")

        execute = Browser()

        for line in inputFile:
            commands = line.split()

            if commands[0] == "NAVIGATE":
                execute.navigate_to(commands[1])

            elif commands[0] == "BACK":
                execute.back()
                
            elif commands[0] == "FORWARD":
                execute.forward()

            elif commands[0] == "HISTORY":
                execute.history()
            
            else:
                raise Exception("Invalid input")
