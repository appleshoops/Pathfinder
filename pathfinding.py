# A Python Pathfinding App By Ethan Eswaran
# Import The Pygame and Maths Library
import pygame
import math
from queue import PriorityQueue
import heapq



pygame.init()

window_size = (800, 800)
square_size = 30

screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("A* Pathfinding App")


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

        
pygame.quit
