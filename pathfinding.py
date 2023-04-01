import pygame
from pygame.locals import *
import math
import random
import numpy as np
import sys
import time
import pathfind
from pathfind.finder import Dijkstra
from pathfind.graph import Grid
from pathfind import Direction


pygame.init()

green = (163, 247, 180)
red = (250, 145, 152)
white = (255, 255, 255)
grey = (156, 156, 156)
screen_size = (600, 600)

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Pathfinding")

m = []
path = 0

blockPlaceX = 10
blockPlaceY = 10

placeStart = 0
placeEnd = 0

placeStartX = 1
placeStartY = 1
placeEndX = 3
placeEndY = 3

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    pressed = pygame.key.get_pressed()

    def clearAll():
        global placeStart, placeEnd
        placeStart = 0
        placeEnd = 0
        r = -1
        c = 0
        for row in m:
            r = +1
            c = -1
            for cell in m:
                c = +1
                m[r][c] = 0


    def findPath():
        global placeEndX, placeEndY, placeStartX, placeStartY, path, grid, blockPlaceX, blockPlaceY, graph, pathfind
        graph = pathfind.transform.matrix2graph(m, diagonal=True)
        path = pathfind.find(graph, start = "placeStartX, placeStartY", end = "placeEndX, placeEndY", method="Djikstra")

    if pressed[pygame.K_z]:
        findPath()

    print(path)
    screen.fill(white)

    pygame.display.update()

    pygame.time.delay(100)

