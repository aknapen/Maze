'''
Created December 24, 2018
    
@author: Alexander Knapen
'''

class Cell:
    
    def __init__(self, x, y, maze_width, maze_height):
        
        self.x = x # X-coordinate location
        
        self.y = y # Y-coordinate location
        
        self.wall = True # Whether cell is wall or not
        
        self.adjacent_cells = {} # Dictionary of 3 or 4 adjacent cells
        self.set_adjacent_cells()

    
    # Function to return state of cell (i.e. whether the cell is a wall or a path
    def is_wall(self):
        return self.wall
    
    # Function to change state of cell to a path
    def set_as_path(self):
        self.wall = False
    
    # Function to set the adjacency list of cell
    def set_adjacent_cells(self):
            self.adjacent_cells["West"] = (self.x-1, self.y)
            self.adjacent_cells["North"] = (self.x, self.y-1)
            self.adjacent_cells["East"] = (self.x+1, self.y)
            self.adjacent_cells["South"] = (self.x, self.y+1)
    
    def get_adjacent_cells(self):
        return [self.adjacent_cells["North"], 
                self.adjacent_cells["South"], 
                self.adjacent_cells["East"], 
                self.adjacent_cells["West"]]
    
    def get_adjacent_cells_with_labels(self):
        return ["North: " + str(self.adjacent_cells["North"]), 
                'East: ' + str(self.adjacent_cells["East"]), 
                'South: ' + str(self.adjacent_cells["South"]), 
               'West: ' + str(self.adjacent_cells["West"])]
    

cell1 = Cell(2, 3)
print(cell1.get_adjacent_cells_with_labels())
print(cell1.is_wall())
cell1.set_as_path()
print(cell1.is_wall())
