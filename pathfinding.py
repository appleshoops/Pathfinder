import pygame
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
grid = [[white for j in range(num_cols)] for i in range(num_rows)]

screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("A* Pathfinding App")
font = pygame.font.SysFont(None, 24)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        # Check for mouse button events
        if event.type == MOUSEBUTTONDOWN:
            # Check for left mouse button click
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                row = mouse_pos[1] // square_size
                col = mouse_pos[0] // square_size
                grid[row][col] = green
            # Check for right mouse button click
            elif event.button == 3:
                mouse_pos = pygame.mouse.get_pos()
                row = mouse_pos[1] // square_size
                col = mouse_pos[0] // square_size
                grid[row][col] = red

    screen.fill(white)

    for row in range(num_rows):
        for col in range(num_cols):
            rect = pygame.Rect(col * square_size, row *
                               square_size, square_size, square_size)
            pygame.draw.rect(screen, grid[row][col], rect)

    pygame.display.update()
