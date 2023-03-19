import pygame
import math
from queue import PriorityQueue
import heapq
from pygame.locals import *


pygame.init()

green = (163, 247, 180)
red = (250, 145, 152)
white = (255, 255, 255)
grey = (156, 156, 156)

window_size = (600, 600)
square_size = 30
num_rows = 20
num_cols = 20
grid = [[(white) for j in range(num_cols)]for i in range(num_rows)]

screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("A* Pathfinding App")
font = pygame.font.SysFont(None, 24)

draw_green = True

while True:

    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        pressed = pygame.key.get_pressed()
        if pressed [pygame.K_TAB]:
         mouse_pos = pygame.mouse.get_pos()
         row = mouse_pos[1] // square_size
         col = mouse_pos[0] // square_size
         grid[row][col] = grey
        
        if pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_pos[1] <= 30:
                draw_green = not draw_green
            else:
                row = mouse_pos[1] // square_size
                col = mouse_pos[0] // square_size
                if draw_green:
                    if grid[row][col] != white:
                        for i in range(num_rows):
                            for j in range(num_cols):
                                if grid[i][j] == green:
                                    grid[i][j] = white
                    grid[row][col] = green

        if pygame.mouse.get_pressed()[2]:
            mouse_pos = pygame.mouse.get_pos()
            row = mouse_pos[1] // square_size
            col = mouse_pos[0] // square_size
            grid[row][col] = red
            for i in range(num_rows):
                for j in range(num_cols):
                    if i != row or j != col:
                        if grid[i][j] == red:
                            grid[i][j] = white
                            
    screen.fill(white)

    for row in range(num_rows):
        for col in range(num_cols):
            rect = pygame.Rect(col * square_size, row *
                               square_size, square_size, square_size)
            pygame.draw.rect(screen, grid[row][col], rect)

    pygame.display.update()

    pygame.time.delay(100)
