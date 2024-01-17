'''
Sudoku Solver
-------------------------------------------------------------
pip install pygame
image link:
https://www.pngitem.com/pimgs/m/210-2106648_empty-sudoku-grid-grid-6x6-png-transparent-png.png
'''

import pygame

pygame.fontinit()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('SUDOKU SOLVER USING BACKTRACKING')
img = pygame.image.load('icon.png')
pygame.display.set_icon(img)
font1 = pygame.font.SysFont('comicsans', 40)
font2 = pygame.font.SysFont('comicsans', 20)
x = 0
y = 0
dif = 500 / 9
val = 0

# Default Sudoku Board
grid = [
   [7, 8, 0, 4, 0, 0, 1, 2, 0],
   [6, 0, 0, 0, 7, 5, 0, 0, 9],
   [0, 0, 0, 6, 0, 1, 0, 7, 8],
   [0, 0, 7, 0, 4, 0, 2, 6, 0],
   [0, 0, 1, 0, 5, 0, 9, 3, 0],
   [9, 0, 4, 0, 6, 0, 0, 0, 5],
   [0, 7, 0, 3, 0, 0, 0, 1, 2],
   [1, 2, 0, 0, 0, 7, 4, 0, 0],
   [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

def get_coord(pos):
    x = pos[0] // diff
