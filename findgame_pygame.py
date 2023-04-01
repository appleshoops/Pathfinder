from tkinter import messagebox as tk
import pygame
import sys

width = 600
height = 600

columns = 30
rows = 30

square_width = width // columns
square_height = height // rows

grid = []

class square:
    def __init__(self, i, j):
        self.x = i
        self.y = j
        self.start = False
        self.wall = False
        self.end = False
    def draw(self, win, colour):
        pygame.draw.rect(win, colour, (self.x * square_width, self.y * square_height, square_width - 2, square_height -2))

for i in range(columns):
    arr = []
    for j in range(rows):
        arr.append(square(i, j))
    grid.append(arr)

start_square = grid[0][0]
start_square.start = True

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pathfinding App")

def main():
    begin_search = False
    target_square_set = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                if event.buttons[0]:
                    i = x // square_width
                    j = y // square_height
                    grid[i][j].wall = True
                if event.buttons[2] and not target_square_set:
                    i = x // square_width
                    j = y // square_height
                    end_square = grid[i][j]
                    end_square.end = True
                    end_square_set = True
            if event.type == pygame.KEYDOWN and target_square_set:
                begin_search = True

        window.fill('grey22')

        for i in range(columns):
            for j in range(rows):
                square = grid[i][j]
                square.draw(window, "gray8")
                if square.start:
                    square.draw(window, "green")

        pygame.display.flip()

main()

pygame.display.update()
