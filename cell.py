class Cell:
    
    def __init__(self, x, y, maze_width, maze_height):
        
        self.x = x # X-coordinate location
        
        self.y = y # Y-coordinate location
        
        self.wall = True # Whether cell is wall or not
        
        self.maze_width = maze_width # Width of maze - needed to set adjacent cells
        
        self.maze_height = maze_height # Height of maze - needed to set adjacent cells
        
        self.adjacent_cells = {} # Dictionary of 3 or 4 adjacent cells
        self.set_adjacent_cells()
        
        self.is_interior = True

    
    # Function to return state of cell (i.e. whether the cell is a wall or a path
    def is_wall(self):
        return self.wall
    
    # Function to change state of cell to a path
    def set_as_path(self):
        self.wall = False
    
    # Function to set the adjacency list of cell
    def set_adjacent_cells(self):
            if self.y - 1 < 0:
                self.adjacent_cells["North"] = None
                self.is_interior = False
            else:
                self.adjacent_cells["North"] = (self.x, self.y-1)
            if self.x + 1 == self.maze_width:
                self.adjacent_cells['East'] = None
                self.is_interior = False
            else:   
                self.adjacent_cells["East"] = (self.x+1, self.y)
            if self.y + 1 == self.maze_height:
                self.adjacent_cells['South'] = None
                self.is_interior = False
            else:  
                self.adjacent_cells["South"] = (self.x, self.y+1)
            if self.x - 1 < 0:
                self.adjacent_cells['West'] = None
                self.is_interior = False
            else: 
                self.adjacent_cells["West"] = (self.x-1, self.y)
    
    def get_adjacent_cells(self):
        return [self.adjacent_cells["North"], 
                self.adjacent_cells["East"], 
                self.adjacent_cells["South"], 
                self.adjacent_cells["West"]]
        
    def get_adjacent_cells_with_labels(self):
        return ["North: " + str(self.adjacent_cells["North"]), 
                'East: ' + str(self.adjacent_cells["East"]), 
                'South: ' + str(self.adjacent_cells["South"]), 
               'West: ' + str(self.adjacent_cells["West"])]
    

cell1 = Cell(2, 3, 40, 40)
print(cell1.get_adjacent_cells())
print(cell1.is_wall())
cell1.set_as_path()
print(cell1.is_wall())