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
    def draw(self, win, colour):
        pygame.draw.rect(win, colour, (self.x * square_width, self.y * square_height, square_width - 2, square_height -2))

for i in range(columns):
    arr = []
    for j in range(rows):
        arr.append(square(i, j))
    grid.append(arr)

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pathfinding App")

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        window.fill('grey22')

        for i in range(columns):
            for j in range(rows):
                square = grid[i][j]
                square.draw(window, "gray8")

        pygame.display.flip()

main()

pygame.display.update()
