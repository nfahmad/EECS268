'''
Author: Nabeel Ahmad
KUID: 3096518
Date: 02/21/2023
Lab: lab4
Last modified: 02/21/2023
Purpose: Creates a Node class.
'''

#node.py

#makes a Node class
class Node:

    #initializes entry
    def __init__(self, entry, nextNode = None):
        self.entry = entry
        
        self.next = nextNode