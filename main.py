# Snake game for ANN
# Andres Morales 2020

import pygame as pg 
import sys

from pygame.locals import *
from pygame import draw as dp

from snake import Snake
from grid import Grid

import numpy as np

# Basic Setup 
pg.init()
DIM = {
    "x": 700,
    "y": 500
}
dimension = (DIM["x"], DIM["y"])
square_dimension = 25

UPDATE_EVENT = 1

'''
Main function - Executed each iteration
'''    

def main(): 
    screen = pg.display.set_mode(dimension)
    screen.fill((0,0,0))
    pg.display.set_caption("Snake - IA")
    # Game Variables 
    amount_of_squares = (DIM["x"] / square_dimension, DIM["y"] / square_dimension)
    snake = Snake(amount_of_squares) # Main player - snake of Segments()
    my_grid = Grid(dimension, square_dimension)
    
    pg.time.set_timer(UPDATE_EVENT, 150)

    keep_adding = True
    # Game loop
    while True:
        # Key 
        key = pg.key.get_pressed()
        temp_direction = snake.segments[0].direction
        if key[pg.K_UP] and temp_direction[1] != 1:
            snake.move(np.array([0, -1]))
        elif key[pg.K_DOWN] and temp_direction[1] != -1:
            snake.move(np.array([0, 1]))
        elif key[pg.K_LEFT] and temp_direction[0] != 1:
            snake.move(np.array([-1, 0]))
        elif key[pg.K_RIGHT] and temp_direction[0] != -1:
            snake.move(np.array([1, 0]))
        elif key[pg.K_SPACE] and keep_adding:
            snake.add_segment()
            keep_adding = False
        '''
        Events handler
        '''
        for event in pg.event.get():
            if event.type == UPDATE_EVENT: 
                snake.update(my_grid)
            if event.type == QUIT:
                print('Quitting game...')
                sys.exit(0) 
        '''
        Game Functions 
        '''
        screen.fill((0,0,0))

        my_grid.display(screen)
        snake.display(my_grid)

        pg.display.update()        
    return 0

if __name__ == "__main__":
    pg.init()
    main()