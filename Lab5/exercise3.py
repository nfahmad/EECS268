'''
Author: Nabeel Ahmad
KUID: 3096518
Date: 02/25/2023
Lab: lab5
Last modified: 02/28/2023
Purpose: Takes an integer and a mode from the user. If the mode is "i", then the user will recieve a fibonacci number for that number. If the mode is "v", then the user will recieve an indication of if their number is in the fibonacci sequence or not
'''

#exercise3.py

#returns fibonacci number for the given number
def fibonacci_i(num):
    if num == 0:
        return 0

    elif num == 1:
        return 1

    else:
        return (fibonacci_i(num - 1) + fibonacci_i(num - 2))

#returns an indication of whether or not the given number is in the fibonacci sequence
def fibonacci_v(result, num = 0):
    if (fibonacci_i(num)) < result:
        fibonacci_v(result, num + 1)

    elif (fibonacci_i(num)) == result:
        return print(f"{result} is in the sequence")
    
    elif (fibonacci_i(num)) > result:
        return print(f"{result} is not in the sequence")

#runs both methods and interacts with the user
def main():
    userInput = input("Enter mode and value: ")

    commandList = userInput.split(" ")

    command = commandList[0]

    identify = int(commandList[1])

    if identify < 0:
        print("Invalid number")

    elif command == "-i":
        print(fibonacci_i(identify))
    
    elif command == "-v":
        fibonacci_v(identify)
    
    else:
        print("Invalid input")

main()