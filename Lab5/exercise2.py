'''
Author: Nabeel Ahmad
KUID: 3096518
Date: 02/25/2023
Lab: lab5
Last modified: 02/28/2023
Purpose: Ask the user for what day they want a count of people with the flu for. Then display the amount
'''

#exercise2.py

#provides a method for identifying how many people have the flu based on the given number
def outbreak(day):
    day1 = 6

    day2 = 20

    day3 = 75

    if day == 1:
        return day1
    
    elif day == 2:
        return day2

    elif day == 3:
        return day3
    
    else:
        return outbreak(day - 1) + outbreak(day - 2) + outbreak(day - 3)

#interacts with the user and runs the outbreak method
def main():
    print("OUTBREAK!")
    
    userInput = int(input("What day do you want a sick count for?: "))

    if userInput <= 0:
        print("Invalid day")

    else:
        print(f"Total people with flu: {outbreak(userInput)}")

main()
