import numpy as np

'''
@class Segment
'''
class Segment:
    '''
    Constructor 
        Overloaded constructor which recieves either np.array or x and y components for 
        segment position
    '''
    def __init__(self, direction, posx, posy = 0):
        self.direction = direction
    
        if type(posx) == np.ndarray:
            self.pos = posx # numpy array with positions
        else:
            self.pos = np.array([posx, posy])
        

    '''
    Draw 

    '''

    def draw(self, grid):
        grid.mat[self.pos[0]][self.pos[1]] = 2
        