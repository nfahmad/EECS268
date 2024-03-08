'''
Author: Nabeel Ahmad
KUID: 3096518
Date: 03/15/2023
Lab: lab6
Last modified: 03/29/2023
Purpose: Contains a main function.
'''

#main.py

from executive import Executive

import sys

#serves as the main function that runs the class and makes it so that you can add the file to the program directly from the command line
def main(filename=sys.argv[1]):

    my_exec = Executive(filename)

    my_exec.execute()

if __name__ == "__main__":
    main()