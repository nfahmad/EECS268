'''
Author: Nabeel Ahmad
KUID: 3096518
Date: 02/14/2023
Lab: lab3
Last modified: 02/14/2023
Purpose: Contains a main function.
'''

#main.py

from cpu_scheduler import CPU_Scheduler

#serves as the main function that runs the classes
def main():
    filename = input("Enter the name of the input file: ")

    my_scheduler = CPU_Scheduler(filename)

    my_scheduler.run()

if __name__ == "__main__":
    main()
