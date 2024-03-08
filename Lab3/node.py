'''
Author: Nabeel Ahmad
KUID: 3096518
Date: 02/14/2023
Lab: lab3
Last modified: 02/14/2023
Purpose: Creates a Node class.
'''

#node.py

#makes a Node class
class Node:

    #initializes entry
    def __init__(self, entry):
        self.entry = entry
        
        self.next = None
