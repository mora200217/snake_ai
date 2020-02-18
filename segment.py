import numpy as np
class Segment:
    def __init__(self, posX, posY):
        self.pos = np.array([posX, posY])
    
    def sayHi(self): 
        print("hi")

    def draw(self, grid):
        pass
        