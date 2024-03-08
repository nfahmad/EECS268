'''
Author: Nabeel Ahmad
KUID: 3096518
Date: 02/05/2023
Lab: lab2
Last modified: 02/07/2023
Purpose: Contains a Function class. Deals with exception handling and storing information from the raiseFunction function in the Process class.
'''

#function.py

#makes a Function class
class Function:

    #initializes name and exceptionHandling
    def __init__(self, name, exceptionHandling):
        self.name = name
        
        self.exceptionHandling = exceptionHandling
    
    #string magic method for returning exceptionHandling and name
    def __str__(self):
        return f"{self.exceptionHandling}, {self.name}"
