'''
Author: Nabeel Ahmad
KUID: 3096518
Date: 03/15/2023
Lab: lab6
Last modified: 03/29/2023
Purpose: After receiving a file from command, outputs the path of the flood to the screen. Every space that was flooded will have a "~" to indicate it was flooded. Also, indicates if the flood ran out of water or if it flooded the accessible area completely.
'''

#executive.py

#creates an Executive class
class Executive:

    #initialize the file and create three lists based on different information obtained from the file
    def __init__(self, filename):
        self.filename = filename

        try:
            inputFile = open(filename, "r")

        except:
            raise Exception(FileNotFoundError)

        self.directions = []

        self.maze = []

        self.coordinates = []

        for line in inputFile:
            line = list(line)

            if line[-1] == "\n":
                line.pop

            self.directions.append(line)
        
        try:
            len(list(self.directions[2::]))

            len(self.directions[2][0])
        
        except:
            raise Exception("The number of rows or columns provided is less than zero")

        for areas in self.directions[2::]:
            self.maze.append(areas)
        
        self.rowLocation = int("".join(self.directions[0][2::]))

        self.colLocation = int(self.directions[0][0])

        self.floodLimit = int("".join(self.directions[1]))

        self.startingFloodLimit = self.floodLimit

        self.maximum = 0

        for line in self.maze:
            for coordinate in line:
                if coordinate == " ":

                    self.maximum += 1

        if self.floodLimit > self.maximum:

            self.floodLimit = self.maximum
    
    #prints the maze in its current state
    def printMaze(self):
        for line in self.maze:
            for coordinate in line:
                print(coordinate, end="")

        print("")
    
    #determines if the given maze is floodable
    def isFloodable(self, row, col):
        if row >= 0 and row <= (len(self.maze[0]) - 1) and col >= 0 and col <= (len(self.maze) - 1):
            if self.maze[col][row] == " ":
                return True
            
            else:
                return False
            
        else:
            return False
    
    #floods the given maze with water
    def floodMaze(self, row, col):
        if self.floodLimit != 0 and (self.maze[col][row - 1] == " " or self.maze[col + 1][row] == " " or self.maze[col][row + 1] == " " or self.maze[col - 1][row] == " "):
            if self.maze[col][row] == " ":
                self.maze[col][row] = "~"

                self.floodLimit -= 1

                self.coordinates.append([col, row])

                self.floodMaze(self.coordinates[-1][1], self.coordinates[-1][0])

            if self.maze[col][row + 1] == " ":
                self.maze[col][row + 1] = "~"

                self.floodLimit -= 1

                row += 1

                self.coordinates.append([col, row])

                if row >= 0 and row <= len(self.maze[col]):
                    self.floodMaze(self.coordinates[-1][1], self.coordinates[-1][0])
            
            if self.maze[col + 1][row] == " ":
                self.maze[col + 1][row] = "~"

                self.floodLimit -= 1

                col += 1

                self.coordinates.append([col, row])

                if col >= 0 and col <= len(self.maze):
                    self.floodMaze(self.coordinates[-1][1], self.coordinates[-1][0])
            
            if self.maze[col][row - 1] == " ":
                self.maze[col][row - 1] = "~"

                self.floodLimit -= 1

                row -= 1

                self.coordinates.append([col, row])

                if row >= 0 and row <= len(self.maze[col]):
                    self.floodMaze(self.coordinates[-1][1], self.coordinates[-1][0])
            
            if self.maze[col - 1][row] == " ":
                self.maze[col - 1][row] = "~"

                self.floodLimit -= 1

                col -= 1

                self.coordinates.append([col, row])

                if row >= 0 and row <= len(self.maze[col]):
                    self.floodMaze(self.coordinates[-1][1], self.coordinates[-1][0])

        elif self.floodLimit > 0 and len(self.coordinates) != 0:
            self.coordinates.pop()

            if len(self.coordinates) != 0:
                self.floodMaze(self.coordinates[-1][1],self.coordinates[-1][0])

            else:
                updatedMaximum = 0

                for line in self.maze:
                    for coordinate in line:
                        if coordinate == "~":
                            updatedMaximum += 1

                self.maximum = updatedMaximum

                return True
        else:
            return True
    
    #executes the flooding of the maze
    def execute(self):
        if self.isFloodable(self.rowLocation, self.colLocation):
            if self.isFloodable(self.rowLocation, self.colLocation):
                self.floodMaze(self.rowLocation, self.colLocation)

                print(f"Size: {len(self.maze)},{len(self.maze[0]) - 1}")

                print(f"Starting Position: {self.colLocation},{self.rowLocation}")

                self.printMaze()

                updatedMaximum = 0

                for line in self.maze:
                    for coordinate in line:
                        if coordinate == "~":
                            updatedMaximum += 1

                self.maximum = updatedMaximum

                if self.startingFloodLimit <= self.maximum:
                    print("Flood ran out of water.")

                else:
                    print("Flood complete.")

            else:
                print("Invalid starting position")
            
        else:
            print("Invalid starting position")
