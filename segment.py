import numpy as np

'''
@class Segment
'''
class Segment:
    def __init__(self, pos, posy = 0):
        if type(pos) == np.ndarray:
            self.pos = pos
        else:
            self.pos = np.array([pos, posy])
        



    def draw(self, grid):
        grid.mat[self.pos[0]][self.pos[1]] = 2
        