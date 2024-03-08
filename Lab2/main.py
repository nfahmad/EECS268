'''
Author: Nabeel Ahmad
KUID: 3096518
Date: 02/07/2023
Lab: lab2
Last modified: 02/07/2023
Purpose: Contain a main function.
'''

#main.py

from process import Process

#serves as the main function that runs the classes
def main():
    filename = input("Enter the name of the input file: ")

    my_process = Process(filename)

    my_process.run()

if __name__ == "__main__":
    main()
