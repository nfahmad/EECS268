'''
Author: Nabeel Ahmad
KUID: 3096518
Date: 04/18/2023
Lab: lab8
Last modified: 04/19/2023
Purpose: Contain a main function.
'''

#main.py

from executive import Executive

#serves as the main function that runs the classes
def main():
    file_name = input("Enter the name of the input file: ")

    print(" ")

    my_exec = Executive(file_name)

    my_exec.run()

if __name__ == "__main__":
    main()