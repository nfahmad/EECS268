'''
Author: Nabeel Ahmad
KUID: 3096518
Date: 04/18/2023
Lab: lab8
Last modified: 04/19/2023
Purpose: Creates a binary node class.
'''

#binarynode.py

#makes a binary node class
class BinaryNode:

    #initializes entry
    def __init__(self, entry):
        self.entry = entry

        self.left = None
        
        self.right = None
