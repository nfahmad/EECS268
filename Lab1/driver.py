'''
Author: Nabeel Ahmad
KUID: 3096518
Date: 01/31/2023
Lab: lab1
Last modified: 01/31/2023
Purpose: Contain a main function.
'''

#driver.py

from executive import Executive

#serves as the main function that runs the classes
def main():
    file_name = input("Enter the name of the input file: ")

    my_exec = Executive(file_name)

    my_exec.run()

if __name__ == "__main__":
    main()

