import pygame as pg
from random import random
from collections import deque

green = (163, 247, 180)
red = (250, 145, 152)
white = (255, 255, 255)
grey = (156, 156, 156)

def get_rect(x, y):
    return x * Tile + 1, y * Tile + 1, Tile - 2, Tile - 2
cols, rows = 30, 30
Tile = 60

pg.init()
sc = pg.display.set_mode([cols * Tile, rows * Tile])
clock = pg.time.Clock()

grid = [[1 if random() < 0.2 else 0 for col in range(cols)] for row in range(rows)]

while True:
    sc.fill(pg.color.Color('black'))

    

    [exit() for event in pg.event.get() if event.type == pg.QUIT]
    pg.display.flip()
    clock.tick(7)
