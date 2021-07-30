
import unittest
import sys
import os
# import pytest

sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))
from TeamLauraAlgo import TeamLauraAlgo

mg = TeamLauraAlgo()

class Test(unittest.TestCase):

    def test_setdim(self):
        mg.setDimCols(10)
        print(mg.dimCols)
        self.assertTrue(mg.dimCols ==10)
        mg.setDimRows( 20)
        self.assertTrue(mg.dimRows == 20)
        self.assertRaises(Exception, mg.setDimRows, -10)

    def test_setstart(self):
        mg.setStartRow


class MazeNeighbours(unittest.TestCase):

    def test_neighbors(self):
        mg.loadMaze(os.path.realpath(os.path.dirname(__file__))
            + "/../../../MazeExamples/maze1.txt")
        lResult = mg.getNeighbours(0,0)
        self.assertTrue(len(lResult) == 2)
        self.assertTrue(lResult == [[1,0], [0,1]])
        lResult = mg.getNeighbours(3,2)
        self.assertTrue(len(lResult) == 3)


class FillMazeTest(unittest.TestCase):
    def test_loadmaze(self):
       self.assertTrue(mg.loadMaze(os.path.realpath(os.path.dirname(__file__))+
                 "/../../../MazeExamples/maze1.txt"))
       self.assertFalse(mg.loadMaze(os.path.realpath(os.path.dirname(__file__))+
                  "/../../MazeExamples/maze1.txt"))

    def test_tostring(self):
        self.assertTrue(mg.gridElementToString(1,2) == "1-2" )

    def test_sameelement(self):
        self.assertFalse(mg.isSameGridElement([2,1],[1,2]))
        self.assertTrue(mg.isSameGridElement([2,1],[2,1]))

    def test_heuristic(self):
        self.assertTrue(mg.heuristic([0, 0], [3, 4]) == 7)
        
   
    # def test_isingrid(self):
    #    self.assertTrue(mg.loadMaze(os.path.realpath(os.path.dirname(
    #        __file__))+"/../../../MazeExamples/maze1.txt"))
    #    self.assertTrue(mg.isInGrid(0, 0))
