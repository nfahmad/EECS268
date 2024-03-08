'''
Author: Nabeel Ahmad
KUID: 3096518
Date: 04/18/2023
Lab: lab8
Last modified: 04/19/2023
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
        
        self.countCopyAmount = 0

    #print menu
    def menu(self):
        print("1) Search Pokedex")

        print("2) Add to Pokedex")

        print("3) Print Pokedex in certain order")

        print("4) Remove from Pokedex")

        print("5) Copy Pokedex")

        print("6) Quit\n")
    
    #run user input
    def run(self):
        userInput = 0

        while userInput != "6":
            self.menu()

            userInput = input("Enter a choice: ")

            print(" ")

            if userInput == "1":
                if self.countCopyAmount == 0:
                    try:
                        searchInput = int(input("Enter a pokedex number: "))
                    
                    except ValueError:
                        print("Try again with a number.\n")

                        continue

                    if self.binarytree.search(searchInput):
                        print(" ")
                    
                    else:
                        print("Pokedex number not found.\n")
            
                else:
                    binaryTreeSelector = input("Which binary tree do you want to search from? ('original' or 'copy'): ")
                    
                    print(" ")

                    try:
                        searchInput = int(input("Enter a pokedex number: "))
                    
                    except ValueError:
                        print("Try again with a number.\n")

                        continue

                    if binaryTreeSelector == "copy":
                        if copybinarytree.search(searchInput):
                            print(" ")
                        
                        else:
                            print("Pokedex number not found.\n")

                    elif binaryTreeSelector == "original":
                        if self.binarytree.search(searchInput):
                            print(" ")
                        
                        else:
                            print("Pokedex number not found.\n")
                    
                    else:
                        print("Invalid input")

            elif userInput == "2":
                if self.countCopyAmount == 0:
                    americanName = input("Enter an American Pokemon name: ")

                    try:
                        addInput = int(input("Enter a pokedex number: "))

                    except ValueError:
                        print("Try again with a number.\n")

                        continue

                    japaneseName = input("Enter a Japanese Pokemon name: ")

                    print(" ")

                    try:
                        self.binarytree.add(PokedexHandler(americanName, addInput, japaneseName))

                    except RuntimeError:
                        print("No duplicate Pokemons are allowed.\n")

                else:
                    binaryTreeSelector = input("Which binary tree do you want to add to? ('original' or 'copy'): ")
                    
                    print(" ")
                    
                    if binaryTreeSelector == "copy":
                        americanName = input("Enter an American Pokemon name: ")

                        try:
                            addInput = int(input("Enter a pokedex number: "))

                        except ValueError:
                            print("Try again with a number.\n")

                            continue

                        japaneseName = input("Enter a Japanese Pokemon name: ")

                        print(" ")

                        try:
                            copybinarytree.add(PokedexHandler(americanName, addInput, japaneseName))

                        except RuntimeError:
                            print("No duplicate Pokemons are allowed.\n")
                    
                    elif binaryTreeSelector == "original":
                        americanName = input("Enter an American Pokemon name: ")

                        try:
                            addInput = int(input("Enter a pokedex number: "))

                        except ValueError:
                            print("Try again with a number.\n")

                            continue

                        japaneseName = input("Enter a Japanese Pokemon name: ")

                        print(" ")

                        try:
                            self.binarytree.add(PokedexHandler(americanName, addInput, japaneseName))

                        except RuntimeError:
                            print("No duplicate Pokemons are allowed.\n")
                            
                    else:
                        print("Invalid input\n")

            elif userInput == "3":
                if self.countCopyAmount == 0:
                    print("1) Print pre-order")

                    print("2) Print in-order")

                    print("3) Print post-order\n")

                    traversalInput = input("Enter a choice: ")

                    print(" ")

                    if traversalInput == "1":
                        self.binarytree.pre_order()

                        print(" ")
                    
                    elif traversalInput == "2":
                        self.binarytree.in_order()

                        print(" ")
                    
                    elif traversalInput == "3":
                        self.binarytree.post_order()

                        print(" ")
                    
                    else:
                        print("Invalid input")
                
                else:
                    binaryTreeSelector = input("Which binary tree do you want to print? ('original' or 'copy'): ")

                    print(" ")

                    if binaryTreeSelector == "copy":
                        print("1) Print pre-order")

                        print("2) Print in-order")

                        print("3) Print post-order\n")

                        traversalInput = input("Enter a choice: ")
                        
                        if traversalInput == "1":
                            copybinarytree.pre_order()

                            print(" ")
                    
                        elif traversalInput == "2":
                            copybinarytree.in_order()

                            print(" ")
                        
                        elif traversalInput == "3":
                            copybinarytree.post_order()

                            print(" ")
                        
                        else:
                            print("Invalid input\n")

                    elif binaryTreeSelector == "original":
                        print("1) Print pre-order")

                        print("2) Print in-order")

                        print("3) Print post-order\n")

                        traversalInput = input("Enter a choice: ")

                        print(" ")
                        
                        if traversalInput == "1":
                            self.binarytree.pre_order()

                            print(" ")
                    
                        elif traversalInput == "2":
                            self.binarytree.in_order()

                            print(" ")
                        
                        elif traversalInput == "3":
                            self.binarytree.post_order()

                            print(" ")
                        
                        else:
                            print("Invalid input")

                    else:
                        print("Invalid input")
            
            elif userInput == "4":
                if self.countCopyAmount == 0:
                    try:
                        removeInput = int(input("Enter a pokedex number: "))

                        print(" ")
                        if self.binarytree.search(removeInput):
                            self.binarytree.remove(removeInput)

                            print(f"Pokemon with pokedex number {removeInput} has been removed.\n")

                    except ValueError:
                        print("Selected pokemon is not found\n")

                        continue
                    
                else:
                    binaryTreeSelector = input("Which binary tree do you want to remove from? ('original' or 'copy'): ")

                    print(" ")

                    if binaryTreeSelector == "copy":
                        try:
                            removeInput = int(input("Enter a pokedex number: "))

                            print(" ")

                            if copybinarytree.search(removeInput):
                                copybinarytree.remove(removeInput)

                                print(f"Pokemon with pokedex number {removeInput} has been removed.\n")
                        
                        except ValueError:
                            print("Selected pokemon is not found\n")

                            continue

                    elif binaryTreeSelector == "original":
                        try:
                            removeInput = int(input("Enter a pokedex number: "))

                            print(" ")

                            if self.binarytree.search(removeInput):
                                self.binarytree.remove(removeInput)

                                print(f"Pokemon with pokedex number {removeInput} has been removed.\n")
                        
                        except ValueError:
                            print("Selected pokemon is not found\n")
                            
                            continue

                    else:
                        print("Invalid input\n")

            elif userInput == "5":
                if self.countCopyAmount < 1:
                    copybinarytree = self.binarytree.copy()

                    print("Copy of binary tree made.\n")

                    self.countCopyAmount += 1
                
                else:
                    print("A copy binary tree has already been made.\n")
            
            elif userInput == "6":
                break

            else:
                print("Invalid input\n")
