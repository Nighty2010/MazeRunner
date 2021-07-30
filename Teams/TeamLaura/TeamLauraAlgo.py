
"""
Lauras implementation class for the Maze solver
"""

# import sys
# from math import sqrt
import queue
from tkinter.constants import Y
import numpy as np
import os.path


class TeamLauraAlgo:

    EMPTY = 0       # empty cell
    BLOCKED = 1    # cell with obstacle / blocked cell
    START = 2       # the start position of the maze (red color)
    TARGET = 3      # the target/end position of the maze (green color)

    def __init__(self):
        # TODO: this is you job now :-)
        self.master = 0
        self.dimCols = 0
        self.dimRows = 0
        self.startCol = 0
        self.startRow = 0
        self.endCol = 0
        self.endRow = 0
        self.grid = [[]]
        self.came_from = []
        print("\n[TeamLauraAlgo]: Constructor TeamLauraAlgo successfully executed.")

    # Setter method for the maze dimension of the rows (zeile)
    def setDimRows(self, rows):
        if rows < 1:
            raise Exception("Rows < 1 in setDimRows")
        self.dimRows = rows

    # Setter method for the maze dimension of the columns (spalte)
    def setDimCols(self, cols):
        self.dimCols = cols

    # Setter method for the column of the start position
    def setStartCol(self, col):
        self.startCol = col
        

    # Setter method for the row of the start position
    def setStartRow(self, row):
        self.startRow = row
        

    # Setter method for the column of the end position
    def setEndCol(self, col):
        self.endCol = col
        

    # Setter method for the row of the end position
    def setEndRow(self, row):
        self.endRow = row

    # Setter method for blocked grid elements 
    def setBlocked(self, row, col):
        # TODO: this is you job now :-)
        pass

    # Start to build up a new maze
    # HINT: don't forget to initialize all member variables of this class (grid, start position, end position, dimension,...)
    def startMaze(self, columns=0, rows=0):
        # TODO: this is you job now :-)
        pass

    # Start to build up a new maze
    # HINT: don't forget to initialize all member variables of this class (grid, start position, end position, dimension,...)

    # Define what shall happen after the full information of a maze has been received
    def endMaze(self):
        # TODO: this is you job now :-)
        # HINT: did you set start position and end position correctly?
        pass

    # just prints a maze on the command line
    def printMaze(self):
        print("Start: (", self.startRow, ", ", self.startCol, ")")
        print("End: (" , self.endRow, ", ", self.endCol, ")")
        print(self.grid)

    # loads a maze from a file pathToConfigFile
    def loadMaze(self, pathToConfigFile):
        # check whether a function numpy.loadtxt() could be useful
        # https://numpy.org/doc/1.20/reference/generated/numpy.loadtxt.html
        # TODO: this is you job now :-)
        exists = os.path.exists(pathToConfigFile)

        if exists:
            print("[TeamLauraAlgo]: SUCCESS loading file: ", pathToConfigFile)
        else:
            print("[TeamLauraAlgo]: ERROR loading file ", pathToConfigFile)
            return False
        self.grid = np.loadtxt(pathToConfigFile, delimiter = ',')
        self.setDimRows(len(self.grid))
        if self.dimRows > 0:
            self.setDimCols(len(self.grid[0]))
        # alternativ
        (tmp_row, tmp_col) = self.grid.shape

        [tmp_row, tmp_col] = np.where(self.grid == self.START)
        self.setStartRow(tmp_row[0]) # Zeile
        self.setStartCol(tmp_col[0]) # Spalte

        [tmp_row, tmp_col] = np.where(self.grid == self.TARGET)
        self.setEndRow(tmp_row[0]) # Zeile
        self.setEndCol(tmp_col[0]) # Spalte

        return True

    # clears the complete maze
    def clearMaze(self):

        pass

    # Decides whether a certain row,column grid element is inside the maze or outside
    def isInGrid(self, row, column):
        if row < 0 or row >= self.dimRows or column < 0 or column >= self.dimCols:
            return False
        return True

    # Returns a list of all grid elements neighboured to the grid element row,column
    def getNeighbours(self, row, column):
        lNeighbours = []
        if not self.isInGrid(row, column):
            return False
        directions = [(row -1, column), (row +1, column), (row, column-1), (row, column+1)]
        for direction in directions:
            if self.isInGrid(direction[0], direction[1]) and self.grid[direction[0], direction[1]] != self.BLOCKED:
                lNeighbours.append(direction)

        # TODO: Add a Unit Test Case --> Very good example for boundary tests and condition coverage
        return lNeighbours

    # Gives a grid element as string, the result should be a string row,column
    def gridElementToString(self, row, col):
        return f'{row}-{col}'
        # HINT: this method is used as primary key in a lookup table


    # check whether two different grid elements are identical
    # aGrid and bGrid are both elements [row,column]
    def isSameGridElement(self, aGrid, bGrid):
        return aGrid == bGrid


    # Defines a heuristic method used for A* algorithm
    # aGrid and bGrid are both elements [row,column]

    def heuristic(self, aGrid, bGrid):
        # Manhattan distance on q square grid
        # taken from https://www.redblob.com/...
        return abs(aGrid[0]-bGrid[0]) + abs(aGrid[1]-bGrid[1])

        # HINT: a good heuristic could be the distance between to grid elements aGrid and bGrid
        pass

    # Generates the resulting path as string from the came_from list
    def generateResultPath(self, came_from):
        # TODO: this is you job now :-)
        # HINT: this method is a bit tricky as you have to invert the came_from list (follow the path from end to start)
        pass

    def getResultPath(self):
        # TODO: this is you job now :-)
        pass

    #############################
    # Definition of Maze solver algorithm
    #
    # implementation taken from https://www.redblobgames.com/pathfinding/a-star/introduction.html
    #############################
    def myMazeSolver(self):
        frontier = queue.PriorityQueue()
        start = (self.startRow, self.startCol)
        goal = (self.endRow, self.endCol)

        step_count = 0

        frontier.put((0, start))
        step_count= step_count+1
        came_from = dict()
        cost_so_far = dict()
        came_from[start] = None
        cost_so_far[start] = 0

        

        while not frontier.empty():
            tmp = frontier.get()
            current = tmp[1]

            if current == goal:
                break
   
            for next in self.getNeighbours(current[0], current[1]):
                new_cost = cost_so_far[current] + 1
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = self.heuristic(goal, next) #+ new_cost  
                    frontier.put((priority, next))
                    step_count= step_count+1
                    came_from[next] = current
            
        current = (self.endRow, self.endCol)
        
        path = []
        while not self.isSameGridElement(current, start):
            path.append(current)
            current = came_from[current]
        path.append(start)
        path.reverse
        return (path, step_count)


    # Command for starting the solving procedure
    def solveMaze(self):
        print("[TeamLauraAlgo]: start solving maze... ")
        return self.myMazeSolver()


if __name__ == '__main__':
    mg = TeamLauraAlgo()

    # HINT: in case you want to develop the solver without MQTT messages and without always
    #       loading new different mazes --> just load any maze you would like from a file

    mg.loadMaze("..\\..\\MazeExamples\\maze1.txt")
    print("[TeamLauraAlgo]: loaded maze")
    mg.printMaze()

    # solve the maze
    # HINT: this command shall be received from MQTT client in run_all mode
    solution = mg.solveMaze()
    solutionString = str(solution[0])
    step_count = solution[1]
    print("[TeamLauraAlgo]: Result of solving maze: ", solutionString)
    print("[TeamLauraAlgo]: Count: ", step_count)
