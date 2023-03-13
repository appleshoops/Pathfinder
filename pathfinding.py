import pygame
from pygame.locals import *
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

pygame.init()

matrix = [
   [1, 1, 1, 1, 1],
   [0, 1, 1, 1, 1],
   [1, 1, 1, 1, 1],
   [1, 1, 1, 1, 1],
   [1, 1, 1, 1, 1]]

green = (163, 247, 180)
red = (250, 145, 152)
white = (255, 255, 255)
grey = (156, 156, 156)

window_size = (600, 600)
grid = Grid(matrix = matrix)

start = grid.node(0, 0)
end = grid.node(5, 5)

finder = AStarFinder(heuristic = any)

path = finder.find_path(start, end, grid)

print(path)

screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("A* Pathfinding App")
font = pygame.font.SysFont(None, 24)



pygame.display.update()
