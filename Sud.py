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
    x = pos[0] //dif
    y = pos[1] //dif

def draw_box():
    for i in range(2):
        pygame.draw.line(screen, (255, 0, 0), (x * dif-3, (y + i)
                        * dif), (x * dif + dif + 3, (y + i)*dif), 7)
        pygame.draw.line(screen, (255, 0, 0), ((x + i) * dif,
                        y * dif), ((x + i) * dif, y * dif + dif), 7)

def draw():
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                pygame.draw.rect(screen, (0, 153, 153),
                                (i * dif, j * dif, dif + 1, dif + 1))
                text1 = font1.render(str(grid[i][j]), 1, (0, 0, 0))
                screen.blit(text1, (i * dif + 15, j * dif + 15))

    for i in range(10):
        if i % 3 == 0:
            thick = 7
        else:
            thick = 1
        pygame.draw.line(screen, (0, 0, 0), (0, i * dif),
                        (500, i * dif), thick)
        pygame.draw.line(screen, (0, 0, 0), (i * dif, 0),
                        (i * dif, 500), thick)
        
def draw_val(val):