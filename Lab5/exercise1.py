'''
Author: Nabeel Ahmad
KUID: 3096518
Date: 02/25/2023
Lab: lab5
Last modified: 02/28/2023
Purpose: Takes in a base and exponent for the user. If the input is valid, it prints the answer of the base taken to the power given
'''

#exercise1.py

#returns the value of the given base and exponent
def powerFunction(base, power):
    if power == 0:
        return 1
    
    else:
        return base * powerFunction(base, power-1)

#interacts with the user and runs the powerFunction method
def main():
    baseInput = int(input("Enter a base: "))

    while True:
        powerInput = int(input("Enter a power: "))

        if powerInput < 0:
            print("Sorry, your exponent must be zero or larger.")

        else:
            print(f"Answer: {powerFunction(baseInput, powerInput)}")

            break

main()
