'''
Author: Nabeel Ahmad
KUID: 3096518
Date: 02/21/2023
Lab: lab4
Last modified: 02/21/2023
Purpose: Contains a main function.
'''

#main.py

from executive import Executive

#serves as the main function that runs the classes
def main():
    filename = input("Enter the name of the input file: ")

    my_exec = Executive(filename)

if __name__ == "__main__":
    main()
