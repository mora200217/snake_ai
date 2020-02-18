# Snake game for ANN
# Andres Morales 2020

import pygame as pg 
import sys

from pygame.locals import *
from pygame import draw as dp

# Basic Setup 
pg.init()
DIM = {
    "x": 700,
    "y": 500
}
dimension = (DIM["x"], DIM["y"])

'''
    Function for grid creation - Displays a n x n square grid for the game
    Params: [square dimensions]  
    Return: Void
'''
def grid(screen, dim = 20):
    # Draw each square of the grid
    squareColor = pg.Color(255, 255, 255, 80)
    for x_step in range(0, DIM['x'], dim):
        for y_step in range(0, DIM['y'], dim):
            dp.rect(screen, squareColor ,((x_step, y_step), (dim, dim)), 1)

''' 
Main function - Executed each iteration
'''    

def main(): 
    screen = pg.display.set_mode(dimension)
    pg.display.set_caption('Hola mundo!')
    
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
        grid(screen = screen)
        pg.display.update()
        
    return 0

if __name__ == "__main__":
    pg.init()
    main()