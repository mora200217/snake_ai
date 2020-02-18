
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
        self.direction = np.array([1, 0])
        self.head = Segment(self.pos[0], self.pos[1])
        self.segments.append(self.head)
        self.add_segment()
        self.add_segment()
        self.add_segment()
        self.add_segment()
        self.add_segment()


    '''
    Add Segment
    '''
    def add_segment(self):
        self.segments.append(Segment(np.add(self.segments[-1].pos, - self.direction)))
    '''
    Display
        Show the snake drawing each segment
        Params: none
    '''
    def display(self, grid): 
        for segment in self.segments: 
            segment.draw(grid)

