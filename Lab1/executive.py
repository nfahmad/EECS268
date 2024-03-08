'''
Author: Nabeel Ahmad
KUID: 3096518
Date: 01/31/2023
Lab: lab1
Last modified: 01/31/2023
Purpose: Contains an Executive class. Handles the File I/O and user interaction. Creates a list of board games by extracting the information from the file.
'''

#executive.py

from boardgame import BoardGame

#makes an Executive class
class Executive:

    #initializes a method to read in the file name and put the information into a list
    def __init__(self, filename):
        self.games = []

        input_file = open(filename, "r")

        for line in input_file:
            words = line.split()

            self.games.append(BoardGame(words[0], float(words[1]), float(words[2]), int(words[3]), int(words[4]), int(words[5])))
    
    #makes a function that prints all games from highest Gibbons range to lowest Gibbons range
    def gibbons_range_high_low(self):
        for element in sorted(self.games, reverse=True):
            print(element)
    
    #prints all games from a year
    def year_sort(self):

        year = False
        try:
            user_input = int(input("Enter a year: "))
            
            print(" ")

            for objects in self.games:
                if objects.year_published == user_input:
                    print(objects)

                    year = True
        
            if year == False:
                print("No games found")
        
        except:
            print(" ")

            print("Invalid Input")

    #asks the user how much time they have for a game and prints a list of games that the user can play in that time
    def game_time(self):
        try:
            user_input = int(input("How many minutes do you have to play a game?: "))

            print(" ")

            for objects in self.games:
                if objects.maximum_playtime <= user_input:
                    print(objects)
        
        except:
            print(" ")

            print("Invalid Input")

    #obtain a number from the user and print all games where the people's rating and Dr. Gibbons rating are separated by that much or more
    def people_against_gibbons(self):
        try:
            user_input = float(input("Enter a people's rating to compare against Dr. Gibbons' rating: "))

            print(" ")

            for objects in self.games:
                if (abs(objects.gibbons_rating - objects.peoples_rating)) >= user_input:
                    print(objects)
        
        except:
            print(" ")

            print("Invalid input")
    
    #obtain a rank from the user and print all games that have at least that Gibbons rank or better
    def print_ranking(self):
        try:
            user_input = int(input("Enter a ranking: "))
            
            print(" ")

            if user_input > 10:
                    print("Invalid input")

            for objects in self.games:
                if objects.gibbons_rating >= user_input:
                    print(objects)
        except:
            print(" ")

            print("Invalid input")

    #prints the menu to the user
    def menu(self):
        print(" ")
        print("1) Print all games highest Gibbons range to lowest")
        print("2) Print all games from a year")
        print("3) Time for a game?")
        print("4) The People VS Dr. Gibbons")
        print("5) Print based on ranking")
        print("6) Exit the program")

    #runs all of the previous functions
    def run(self):
        while True:
            self.menu()

            user_input = input("Enter a choice: ")

            print(" ")

            if user_input == "1":
                self.gibbons_range_high_low()

            elif user_input == "2":
                self.year_sort()

            elif user_input == "3":
                self.game_time()

            elif user_input == "4":
                self.people_against_gibbons()
            
            elif user_input == "5":
                self.print_ranking()

            elif user_input == "6":
                break

            else:
                print("Invalid input")
