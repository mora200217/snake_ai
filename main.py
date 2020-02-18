# Snake game for ANN
# Andres Morales 2020

import pygame as pg 
import sys

from pygame.locals import *
from pygame import draw as dp

from snake import Snake
from grid import Grid

# Basic Setup 
pg.init()
DIM = {
    "x": 700,
    "y": 500
}
dimension = (DIM["x"], DIM["y"])
square_dimension = 25

'''
Main function - Executed each iteration
'''    

def main(): 
    screen = pg.display.set_mode(dimension)
    pg.display.set_caption('Hola mundo!')
    # Game Variables 
    amount_of_squares = (DIM["x"] / square_dimension, DIM["y"] / square_dimension)
    snake = Snake(amount_of_squares) # Main player - snake of Segments()
    my_grid = Grid(dimension, square_dimension)
    # Game loop
    while True:
        '''
        Events handler
        '''
        for event in pg.event.get():
            if event.type == QUIT:
                print('Quitting game...')
                sys.exit(0) 
        '''
        Game Functions 
        '''
        
        my_grid.display(screen)
        pg.display.update()
        
        
    return 0

if __name__ == "__main__":
    pg.init()
    main()