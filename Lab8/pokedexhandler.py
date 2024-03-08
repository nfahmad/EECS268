'''
Author: Nabeel Ahmad
KUID: 3096518
Date: 04/18/2023
Lab: lab8
Last modified: 04/19/2023
Purpose: Handle the American name, pokedex number, and japanese name. Output syntax handling.
'''

#pokedexhandler.py

#creates a pokedex handling class
class PokedexHandler:

    #initializes american name, pokedex number, and japanese name
    def __init__(self, americanName, pokedexNumber, japaneseName):
        self.americanName = americanName

        self.pokedexNumber = pokedexNumber

        self.japaneseName = japaneseName

    #less than magic method
    def __lt__(self, other):
        if self.pokedexNumber < other:
            return True
        
        else:
            return False
    
    #greater than magic method
    def __gt__(self, other):
        if self.pokedexNumber > other:
            return True
        
        else:
            return False
    
    #equal to magic method
    def __eq__(self, other):
        if self.pokedexNumber == other:
            return True
        
        else:
            return False
    
    #not equal to magic method
    def __ne__(self, other):
        if self.pokedexNumber != other:
            return True

        else:
            return False
    
    #string magic method
    def __str__(self):
        output = f"American Name: {self.americanName} | Pokedex Number: {self.pokedexNumber} | Japanese Name: {self.japaneseName}"
        
        return output
    
