
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
    def __init__(self, grid_dim, grid):
        self.grid = grid
        self.initial_segments = 2
        self.segments = [] # Segments+ array
        self.init_pos = np.array([8, 3])
        self.pos = self.init_pos
        self.head = Segment(np.array([0, 1]), self.pos[0], self.pos[1])
        self.segments.append(self.head)
        self.add_segment(self.initial_segments)

    '''
    Add Segment
    '''
    def add_segment(self, n = 0, **keyargs):
        last_segment = self.segments[-1] if len(self.segments) > 1 else self.segments[0]
        if len(self.segments) > 1:
            self.segments.append(Segment(last_segment.direction, np.add(last_segment.pos, - last_segment.direction)))
        else:
            self.segments.append(Segment(last_segment.direction, last_segment.pos)) # If 
        if n > 1:
            self.add_segment(n - 1)
    '''
    Display
        Show the snake drawing each segment
        Params: none
    '''
    def display(self, grid = None): 
        if grid == None: 
            grid = self.grid
        for segment in self.segments: 
            segment.draw(grid)

    '''
    Update
    '''
    def update(self, grid = 0): 
        last_segment = self.segments[-1]
        segments_reverse = self.segments.copy().reverse()
        for segment in reversed(self.segments.copy()):
            # Check for the head not to hit the body 
            if self.segments[0] != segment and (self.segments[0].pos[0] == segment.pos[0] and self.segments[0].pos[1] == segment.pos[1]):
                self.reset()
            grid.mat[segment.pos[0]][segment.pos[1]] = 0 # Delete last instance in grid 
            segment.pos = np.add(segment.pos, segment.direction)
            last_segment.direction = segment.direction
            
            last_segment = segment
            
        # Update directions
        
    

        
            

    '''
    Move
    '''
    def move(self, indications):
        self.segments[0].direction = indications

    '''
    Reset
        Place snake at center of the display and reduces segment length
    '''
    def reset(self):
        # Delete all displays 
        for segments in self.segments[1:]: 
            self.grid.mat[segments.pos[0]][segments.pos[1]] = 0
        del self.segments[1:]
       
        print(self.segments)
        self.segments[0].pos = np.array([5, 5])
        self.segments[0].direction = np.array([0, 1])
        self.add_segment(1)
        

