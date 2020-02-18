
import numpy as np
from segment import Segment

class Snake: 
    ''' 
    Constructor 
        Intantiates a Snake object with 2 Segments 
        amount of squares = aos
        Params: 
            grid_dim (Tuple) -> (aos in x, aos in y)
    '''
    def __init__(self, grid_dim):
        self.segments = [] # Segments+ array
        self.init_pos = np.array([8, 3])
        self.pos = self.init_pos
        self.head = Segment(np.array([0, 1]), self.pos[0], self.pos[1])
        self.segments.append(self.head)
        self.add_segment()
        self.add_segment()
        self.add_segment()




    '''
    Add Segment
    '''
    def add_segment(self):
        last_segment = self.segments[-1]
        self.segments.append(Segment(last_segment.direction, np.add(last_segment.pos, - last_segment.direction)))
    '''
    Display
        Show the snake drawing each segment
        Params: none
    '''
    def display(self, grid): 
        for segment in self.segments: 
            segment.draw(grid)

    '''
    Update
    '''
    def update(self, grid = 0): 
        last_segment = self.segments[-1]
        segments_reverse = self.segments.copy().reverse()
        for segment in reversed(self.segments): 
            grid.mat[segment.pos[0]][segment.pos[1]] = 0 # Delete last instance in grid 
            segment.pos = np.add(segment.pos, segment.direction)
            last_segment.direction = segment.direction
            last_segment = segment
            

    '''
    Move
    '''
    def move(self, indications):
        self.segments[0].direction = indications

