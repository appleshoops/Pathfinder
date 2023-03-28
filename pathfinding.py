import pygame
import math
from queue import PriorityQueue
import heapq
from pygame.locals import *
import pathfinding
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

pygame.init()

green = (163, 247, 180)
red = (250, 145, 152)
white = (255, 255, 255)
grey = (156, 156, 156)

window_size = (600, 600)
square_size = 30
num_rows = 20
num_cols = 20
cellGrid = [[(white) for j in range(num_cols)]for i in range(num_rows)]

screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("A* Pathfinding App")
font = pygame.font.SysFont(None, 24)

while True:
    grid = Grid(matrix=cellGrid)
    start = startPos
    end = endPos
    

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LSHIFT]:
            mouse_pos = pygame.mouse.get_pos()
            row = mouse_pos[1] // square_size
            col = mouse_pos[0] // square_size
            cellGrid[row][col] = grey

        if pressed[pygame.K_z]:
            mouse_pos = pygame.mouse.get_pos()
            row = mouse_pos[1] // square_size
            col = mouse_pos[0] // square_size
            cellGrid[row][col] = green
            startPos = cellGrid[row][col]
            for i in range(num_rows):
                for j in range(num_cols):
                    if i != row or j != col:
                        if cellGrid[i][j] == green:
                            cellGrid[i][j] = white
        if pressed[pygame.K_x]:
            mouse_pos = pygame.mouse.get_pos()
            row = mouse_pos[1] // square_size
            col = mouse_pos[0] // square_size
            cellGrid[row][col] = red
            endPos = cellGrid[row][col]
            for i in range(num_rows):
                for j in range(num_cols):
                    if i != row or j != col:
                        if cellGrid[i][j] == red:
                            cellGrid[i][j] = white

        if pressed[pygame.K_c]:
            mouse_pos = pygame.mouse.get_pos()
            row = mouse_pos[1] // square_size
            col = mouse_pos[0] // square_size
            cellGrid[row][col] = white
            for i in range(num_rows):
                for j in range(num_cols):
                    if i != row or j != col:
                        if cellGrid[i][j] == white:
                            cellGrid[i][j] = white

    screen.fill(white)

    for row in range(num_rows):
        for col in range(num_cols):
            rect = pygame.Rect(col * square_size, row * square_size, square_size, square_size)
            pygame.draw.rect(screen, cellGrid[row][col], rect)

    pygame.display.update()

    pygame.time.delay(100)
