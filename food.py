import numpy as np

class Food:
    def __init__(self, grid, posx = None, posy = None): 
        self.grid = grid
        if posx != None:
            self.pos = np.array([posx, posy])
        else: 
            self.random_pos()
        
    '''
    Draw
        Displays the food locating it on the grid matrix 
    '''
    def draw(self, grid = None): 
        self.grid.mat[self.pos[0]][self.pos[1]] = 2
        # print("Drawn")

    '''
    Update
        Checks for snake touch 
    '''
    def update(self, snake):
        # Checks for snake pos
        # print(self.pos, snake.segments[0].pos)
        if (self.pos[0] == snake.segments[0].pos[0]) and (self.pos[1] == snake.segments[0].pos[1]):
            self.random_pos()
            snake.add_segment()


    '''
    Update Random pos
    '''
    def random_pos(self, grid = None):
        if grid == None:
            grid = self.grid

        self.pos = np.array([
                np.random.randint(0, grid.amount_of_squares[0]),
                np.random.randint(0, grid.amount_of_squares[1]),
            ])
