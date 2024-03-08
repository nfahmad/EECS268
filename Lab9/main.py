'''
Author: Nabeel Ahmad
KUID: 3096518
Date: 04/25/2023
Lab: lab9
Last modified: 04/26/2023
Purpose: Contains a main function.
'''

#main.py

from executive import Executive

#serves as the main function that runs the classes
def main():
    filename = input("Enter the name of the input file: ")

    print(" ")

    my_exec = Executive(filename)

if __name__ == "__main__":
    main()
