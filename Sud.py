'''
Sudoku Solver
-------------------------------------------------------------
pip install pygame
image link:
https://www.pngitem.com/pimgs/m/210-2106648_empty-sudoku-grid-grid-6x6-png-transparent-png.png
'''

import pygame
from io import BytesIO
import base64
from PIL import Image

# Updated base64 image URL
base64_image_url = (
    "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBwgHBgkIBwgKCgkLDRYPDQwMDRsUFRAWIB0iIiAdHx8kKDQsJCYxJx8fLT0tMTU3Ojo6Iys/RD84QzQ5OjcBCgoKDQwNGg8PGjclHyU3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3N//AABEIAKgAsgMBIgACEQEDEQH/xAAbAAADAAMBAQAAAAAAAAAAAAAABAUCAwYBB//EAE8QAAEDAwAFBAsMCAUEAwEAAAECAwQABREGEhMUISIxQVEVMzQ1UlRhYnOxshYjJDI2QlNxdJGz0nKBkpOUlaLRB0NjdcNEVaHTgsHwJf/EABQBAQAAAAAAAAAAAAAAAAAAAAD/xAAUEQEAAAAAAAAAAAAAAAAAAAAA/9oADAMBAAIRAxEAPwD7jRRRQFFFFAUUVE00MgaK3Pc7gzbpBYUG5TzobS2o9JUfi9WejNBbor5Fos4u1aQMwbhFvlmmyoLwEeRM3uPMWlOSpK9Y4WOJ4dH18TfpZ/wWsMkS394XJjhTu1Vrqy/ggnOTwoPrtFfLWLIjSHSbTQyrnc4y4b6ExlxprjYZy1nOqDjn481T7LdLjpo5oha7xPlR40m3PSpW7ulpUxaFlCQVJwcYGsQOv6sB9ior43pE9L0e92Oj8G4TXYDVpbmxy6+pa4iysJKErPHBHHGf/uqGhVyl6SaYp90KpkBUOC09bLYtZSl5tQwXl4PLVkcx5s9YNB9Uor48J0wf4GXaUZcjeUPvBLu1VrpxIwOVnPNwr65EzurOc52ac5+qg20UUUBRRRQFFFFAUUUUBRRRQaJspmDFdlSVFLLSdZZCSo4+ocT+qp/ujgZxsrj/ACyT+Ss9Ju8Uv9Ee0K06WyZ8SzOSLa80yttKSta0a51cjISObJ6zzdRoMlaSW9IBU3cQCQONskc5/wDhWXuig/RXL+WSf/XTs/tKPTNe2mmaCOdJLekgKRcQScAG2SOPT4FLXW42W726Rb7hEuD0WQgocQbbJGR9YRw+uq8vuiF6Y/hrqPeRPVf7dGgXaUxtiXXmEtsltLLZGueU2VZUVIT8Yc5PRxCDZrbotZrqxLC79LmNtLRF35iW9sW+AVswUcBggH660xtGNEI0tl1ti/mMw/vDMFUeYYzbmchQb1Mc5rsJfyntv2ST7TNVqD55cLFotcLlOlPL0jQucQqUyw1Mbbd4ao1kpQMjAxTt2t+i1zhQYy4V1jC3jEN2JAlNORxjHJUEZ5q61PfFfoU+tVM0HARrPomza7nbAxenTcQBNkOw5S33erKyjP8A+NPzm9H5s61TXGbuiXauEZ1uBJSoAgApV73xBA5j5a6Vk4myz5Eeo1zeht5n3F+M5cHJCeyEHfGmXG29QAKSDqFPFIGukYXkkEHIOsKCK7o3qX8M4TXLjNmZJI5KCO3bIUnp+lTd/Clf2i6zqt2u/wAJ+MijLEwyokRt5U2DpKM7A4HuBj7D1znz8UoDlQoPXb2lA5IJ7h+QNI6xEgY69p4LOmLkkaSHEEgcpWP7dqDk09qdqqoJSc1yHU9vG5MYp1DmjZG5O4eWzihAxgDmvxP7k55oINid1qU9U4i2gknkkY9/2me+DzRE9RlVcH/wB9arYkMynPEJHHQz3BqcfNN5I6/iNP5EwNMYXMoTnnIJJJ6GpHTlUEfVX0qi6Op5ZzSYdwUYx5IpVe8ULk/WAyemVaj0XVrXMVbKtJJZSGnt2C2YkwRpJHuL5D1HpTTVNMQQqUIPcjilVhSmnDAPvmeehJpQgEeWFGMtzsjCnIznsfzE+iFf6jRuHMsqNp5RcqBU5wMEnqecY9b6fTli0lp2EKcgbkeSWKkE8hpVufxPyWxmoI0lSwI4yRrW2NHl6dVxL0UBVGzOFT6FB0pTgu7qHp5GrWcMoUjyZ0Bz2Fc9e1IV5v8wWvbeB5t")

pygame.font.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('SUDOKU SOLVER USING BACKTRACKING')

# Decoding the base64 encoded image data
image_bytes = base64.b64decode(base64_image_url.split(",")[-1])
image = pygame.image.load(BytesIO(image_bytes))
pygame.display.set_icon(image)

font1 = pygame.font.SysFont('comicsans', 40)
font2 = pygame.font.SysFont('comicsans', 20)

# Other elements
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
    text1 = font1.render(str(val), 1, (0, 0, 0))
    screen.blit(text1, (x * dif + 15, y * dif + 15))

def raise_error_1():
    text1 = font1.render('WRONG !!!', 1, (0, 0, 0))
    screen.blit(text1, (20, 570))

def raise_error_2():
    text1 = font1.render('Wrong !!! Not a valid Key', 1, (0, 0, 0))
    screen.blit(text1, (20, 570))

def valid(m, i, j, val):
    for it in range(9):
        if m[i][it] == val:
            return False
        if m[it][j] == val:
            return False
        

    it = i // 3
    jt = j // 3

    for i in range(it * 3, it * 3 + 3):
        for j in range(jt * 3, jt * 3 + 3):
            if m[i][j] == val:
                return False
    return True

def solve(grid, i, j):
    while grid[i][j] != 0:
        if i < 8:
            i += 1
        elif i == 8 and j < 8:
            i = 0
            j += 1
        elif i == 8 and j == 8:
            return True
        
    pygame.event.pump()
    for it in range(1, 10):
        if valid(grid, i, j, it) == True:
            grid[i][j] = it
            x = i
            y = j
            screen.fill((255, 255, 255))
            draw()
            draw_box()
            pygame.display.update()
            pygame.time.delay(20)

            if solve(grid, i, j) == 1:
                return True
            else:
                grid[i][j] = 0
            screen.fill((255, 255, 255))

            draw()
            draw_box()
            pygame.display.update()
            pygame.time.delay(50)
    return False

def instruction():
    text1 = font2.render('PRESS D TO RESET TO DEFAULT / R TO EMPTY\n', 1, (0, 0, 0))
    text2 = font2.render('ENTER VALUES AND PRESS ENTER TO VISUALIZE\n', 1, (0, 0, 0))
    screen.blit(text1, (20, 520))
    screen.blit(text2, (20, 540))

def result():
    text1 = font1.render('FINISHED PRESS R or D\n', 1, (0, 0, 0))
    screen.blit(text1, (20, 570))

run = True
flag_1 = 0
flag_2 = 0
rs = 0
error = 0
while run:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            flag_1 = 1
            pos = pygame.mouse.get_pos()
            get_coord(pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 1 
                flag_1 = 1
            if event.key == pygame.K_RIGHT:
               x += 1
               flag_1 = 1
            if event.key == pygame.K_UP:
               y -= 1
               flag_1 = 1
            if event.key == pygame.K_DOWN:
               y += 1
               flag_1 = 1
            if event.key == pygame.K_1:
               val = 1
            if event.key == pygame.K_2:
               val = 2
            if event.key == pygame.K_3:
               val = 3
            if event.key == pygame.K_4:
               val = 4
            if event.key == pygame.K_5:
               val = 5
            if event.key == pygame.K_6:
               val = 6
            if event.key == pygame.K_7:
               val = 7
            if event.key == pygame.K_8:
               val = 8
            if event.key == pygame.K_9:
               val = 9
            if event.key == pygame.K_RETURN:
               flag_2 = 1

            # If R pressed clear sudoku board
            if event.key == pygame.K_r:
                rs = 0
                error = 0
                flag_2 = 0
                grid = [
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0]
               ]
                
            # If D pressed reset board to default
            if event.key == pygame.K_d:
                rs = 0
                error = 0
                flag_2 = 0
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

    if flag_2 == 1:
        if solve(grid, 0, 0) == False:
            error = 1
        else:
            rs = 1
        flag_2 = 0

    if val != 0:
        draw_val(val)
        if valid(grid, int(x), int(y), val) == True:
            grid[int(x)][int(y)] = val
            flag_1 = 0
        else:
            grid[int(x)][int(y)] = 0
            raise_error_2()
        val = 0

    if error == 1:
        raise_error_1()
    if rs == 1:
        result()
    draw()
    if flag_1 == 1:
        draw_box()
    instruction()

    pygame.display.update()
