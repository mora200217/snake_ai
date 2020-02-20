import pygame as pg 
import numpy as np

class Grid: 
    '''
    Constructor 
        @Params: 
        1. dim (tuple, size = 2) -> (dim x, dim y)
        2. square dim (int)
        3. [color] (pg.Color) = 

    ''' 
    def __init__(self, dim, square_dim, color = (0, 0, 255)): 
        self.dim = dim
        self.pos = (0,0)
        self.square_dim = square_dim
        self.color = color
        self.amount_of_squares = (
            int(self.dim[0] / self.square_dim), 
            int(self.dim[1] / self.square_dim))
        # Representation matrix 
        self.mat = np.zeros(self.amount_of_squares, dtype = int)


    '''
    Display
        Show the grid 
        KEY COLORS 
            - 0 Empty
            - 1 Snake
            - 2 Food
            - 3 Wall - Optional
    '''
    def display(self, screen):
        # Colors definitions
        empty_color = (0, 0, 0) # Blakc
        snake_color = (189, 195, 199) # Blue 
        
        food_color = (192, 57, 43) # Red
        wall_color = (255, 255, 255) # White
        colors = [empty_color,snake_color,food_color,wall_color]

        dim_x, dimy = self.mat.shape
        for sq_x in range(0, dim_x):
            for sq_y in range(0, dimy):
                pg.draw.rect(screen, 
                colors[self.mat[sq_x][sq_y]],
                ((sq_x * self.square_dim, sq_y * self.square_dim), 
                (self.square_dim, self.square_dim)),
                0)
                #1 if self.mat[sq_x][sq_y] == 0 else 0)
        pg.display.flip()
        


