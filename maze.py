'''
Created on Dec 24, 2018

@author: MichaelMoschitto
'''
from cell import *
from stack_array import *
import random as r

# fromt stack_arrayimport stack_array


class Maze:
    '''
    This is the maze class which uses the individual cells to make a grid of cells using a 2d array
    '''


    def __init__(self, maze_width, maze_height):
       
        '''
        Constructor
        '''
        self.maze_width = maze_width
        self.maze_height = maze_height
#         self.maze = [] * self.maze_width
        self.maze = [[Cell(x,y,self.maze_width, self.maze_height) for y in range(self.maze_height)] for x in range(self.maze_width)]
        
    def get_maze_string(self): #This gives us a view of the maze with o being a path and 1 being a wall
        string = ''
        for y in range(self.maze_height):
            for x in range(self.maze_width):
                if self.maze[x][y].is_wall():
                    string += 'x'
                else:
                    string += 'o'
                string += ' '
            string += '\n'
        return string
    
#     def gen_maze(self):
#         dict = {1: 'North', 2: 'East', 3: 'South', 4: 'West'}
#         for x in range(1, self.maze_width - 1):
#             for y in range(1, self.maze_height - 1):
#                 num = r.randint(1,5)
#                 self.maze.adjacent_cells[dict[num]] = 
    def test_gen(self):
        for x in range(1, self.maze_width - 1):
            for y in range(1, self.maze_height - 1):
                num = r.randint(1,101)
                if num % 2 == 0 and self.maze[x][y].is_interior:
                    self.maze[x][y].wall = False
   
        
                
maze1 = Maze(10, 10)
print(maze1.get_maze_string())
print('top left', maze1.maze[0][0].get_adjacent_cells_with_labels())
print('top right', maze1.maze[maze1.maze_width - 1][0].get_adjacent_cells_with_labels())
print('bottom left', maze1.maze[0][maze1.maze_height - 1].get_adjacent_cells_with_labels())
print('bottom right', maze1.maze[maze1.maze_width - 1][maze1.maze_height - 1].get_adjacent_cells_with_labels())
maze1.test_gen()
print(maze1.get_maze_string())

