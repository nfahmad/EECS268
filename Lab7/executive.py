'''
Author: Nabeel Ahmad
KUID: 3096518
Date: 04/04/2023
Lab: lab7
Last modified: 04/05/2023
Purpose: Handle File I/O and user input.
'''

#executive.py

from pokedexhandler import PokedexHandler

from binarytree import BinaryTree

#makes an executive class
class Executive:

    #initialize the file
    def __init__(self, filename):
        self.binarytree = BinaryTree()

        self.pokedex = []

        inputFile = open(filename, "r")

        for line in inputFile:
            pokedexSection = line.split()

            self.pokedex.append(pokedexSection)
        
        for namesNum in self.pokedex:
            self.binarytree.add(PokedexHandler(namesNum[0], int(namesNum[1]), namesNum[2]))

    #search the pokedex
    def searchPokedex(self):
        try:
            searchInput = int(input("Enter a pokedex number: "))

            print(" ")

            self.binarytree.search(searchInput)

        except:
            print(" ")

            print("Invalid input")

    #add to the pokedex
    def addToPokedex(self):
        try:
            newAmericanName = input("Enter an American Pokemon Name: ")

            newPokedexNumber = int(input("Enter a new Pokedex Number: "))

            newJapaneseName = input("Enter a Japanese Pokemon Name: ")

            self.binarytree.add(PokedexHandler(newAmericanName, newPokedexNumber, newJapaneseName))

        except:
            print(" ")

            print("Invalid input")

    #print the pokedex in certain traversal order
    def printPokedex(self):
        try:
            print("1) Print pre-order")

            print("2) Print in-order")

            print("3) Print post-order\n")

            printInput = input("Enter a choice: ")

            print(" ")

            if printInput == "1":
                self.binarytree.pre_order()
        
            elif printInput == "2":
                self.binarytree.in_order()
        
            elif printInput == "3":
                self.binarytree.post_order()
            
            else:
                print("Invalid input")

        except:
            print("Invalid input")

    #print menu
    def menu(self):
        print("1) Search Pokedex")

        print("2) Add to Pokedex")

        print("3) Print Pokedex in certain order")

        print("4) Quit\n")
    
    #run methods
    def run(self):
        while True:
            self.menu()

            userInput = input("Enter a choice: ")

            print(" ")

            if userInput == "1":
                self.searchPokedex()

                print(" ")
            
            elif userInput == "2":
                self.addToPokedex()

                print(" ")

            elif userInput == "3":
                self.printPokedex()

                print(" ")
            
            elif userInput == "4":
                break

            else:
                print("Invalid input")

