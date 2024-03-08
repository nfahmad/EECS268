'''
Author: Nabeel Ahmad
KUID: 3096518
Date: 02/21/2023
Lab: lab4
Last modified: 02/21/2023
Purpose: Creates a Browser class. Contains all of the associated methods
'''

#browser.py

from linkedlist import LinkedList

#creates a Browser class
class Browser:

    #initializes browser
    def __init__(self):
        self.linkedlist = LinkedList()

        self.currentArrow = -1

    #the browser navigates to the given url
    def navigate_to(self, url):
        if self.currentArrow == self.linkedlist.lengthFunction():
            self.linkedlist.insertBack(url)

            self.currentArrow = self.currentArrow + 1
        
        else:
            for website in range(self.linkedlist.lengthFunction() - 1 - self.currentArrow):
                self.linkedlist.remove(self.linkedlist.lengthFunction()-1)

            self.linkedlist.insertBack(url)

            self.currentArrow = self.currentArrow + 1

    #if possible, the browser navigates forward in the history otherwise it keeps focus
    def forward(self):
        if self.currentArrow < self.linkedlist.lengthFunction() - 1:
            self.currentArrow = self.currentArrow + 1
        
        else:
            self.currentArrow = self.linkedlist.lengthFunction()-1

    #if possible, the browser navigates backwards in the history otherwise it keeps focus
    def back(self):
        if self.currentArrow > 0:
            self.currentArrow = self.currentArrow - 1
        
        else:
            self.currentArrow = 0

    #returns a well formatted string with the current history
    def history(self):
        print("Oldest")

        print("===========")

        for website in range(self.linkedlist.lengthFunction()):
            if website == self.currentArrow:
                print(f"{self.linkedlist.get_entry(website)} <==current")

            else:
                print(f"{self.linkedlist.get_entry(website)}")

        print("===========")

        print("Newest")

        print(" ")

