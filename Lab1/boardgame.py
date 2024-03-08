'''
Author: Nabeel Ahmad
KUID: 3096518
Date: 01/30/2023
Lab: lab1
Last modified: 01/31/2023
Purpose: Contain a BoardGame class. Have a less than function, initialize on all of the parts of a line in the input file, and arrange the initialized parts into a string.
'''

#boardgame.py

#makes a BoardGame class
class BoardGame:
    
    #initializes name, gibbons rating, people's rating, year published, minimum players, and maximum playtime
    def __init__(self, name, gibbons_rating, peoples_rating, year_published, minimum_players, maximum_playtime):
        self.name = name
        self.gibbons_rating = gibbons_rating
        self.peoples_rating = peoples_rating
        self.year_published = year_published
        self.minimum_players = minimum_players
        self.maximum_playtime = maximum_playtime

    #compares between the gibbons rating and other ratings
    def __lt__(self, other):
        if self.gibbons_rating < other.gibbons_rating:
            return True

        else:
            return False
    
    #makes a template for all of the information to print into for the output
    def __str__(self):
        output = f"{self.name} ({self.year_published}) [GR={self.gibbons_rating}, PR={self.peoples_rating}, MP={self.minimum_players}, MT={self.maximum_playtime}]"

        return output

