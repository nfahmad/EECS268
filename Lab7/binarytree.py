'''
Author: Nabeel Ahmad
KUID: 3096518
Date: 04/04/2023
Lab: lab7
Last modified: 04/05/2023
Purpose: Creates a binary tree class. Contains all of the associated methods.
'''

#binarytree.py

from binarynode import BinaryNode

#creates a binary tree class
class BinaryTree:

    #initializes binary tree
    def __init__(self):
        self.root = None
    
    #add magic method
    def add(self, entry):
        if self.root == None:
            self.root = BinaryNode(entry)

        else:
            self.rec_add(entry, self.root)

    #recursive add method
    def rec_add(self, entry, cur_node):
        try:
            if entry > cur_node.entry:
                if cur_node.right == None:
                    cur_node.right = BinaryNode(entry)

                else:
                    self.rec_add(entry, cur_node.right)
            
            elif entry < cur_node.entry:
                if cur_node.left == None:
                    cur_node.left = BinaryNode(entry)

                else:
                    self.rec_add(entry, cur_node.left)

            elif entry == cur_node.entry:
                raise RuntimeError

        except RuntimeError:
            if entry == cur_node.entry:
                print(" ")
                
                print("Pokemon already exists in the pokedex")

    #search method
    def search(self, target):
        return self.rec_search(target, self.root)

    #recursive search method
    def rec_search(self, target, cur_node):
        if cur_node == None:
            return False
        
        elif cur_node.entry == target:
            print(cur_node.entry)

            return True
        
        else:
            if self.rec_search(target, cur_node.left):
                return True
            
            if self.rec_search(target, cur_node.right):   
                return True

            return False

    #traverse binary tree in pre-order traversal order and feed into recursion
    def pre_order(self):
        return self.rec_pre_order(self.root)
    
    #traverse binary tree in pre-order traversal order using recursion
    def rec_pre_order(self, cur_node):
        if cur_node != None:
            print(cur_node.entry)
            
            self.rec_pre_order(cur_node.left)

            self.rec_pre_order(cur_node.right)

    #traverse binary tree in in-order traversal order and feed into recursion
    def in_order(self):
        if self.root != None:
            self.rec_in_order(self.root)
    
    #traverse binary tree in in-order traversal order using recursion
    def rec_in_order(self, cur_node):
        if cur_node != None:
            self.rec_in_order(cur_node.left)

            print(cur_node.entry)

            self.rec_in_order(cur_node.right)
    
    #traverse binary tree in post-order traversal order and feed into recursion
    def post_order(self):
        return self.rec_post_order(self.root)

    #traverse binary tree in post-order traversal order using recursion
    def rec_post_order(self, cur_node):
        if cur_node != None:
            self.rec_post_order(cur_node.left)

            self.rec_post_order(cur_node.right)

            print(cur_node.entry)
