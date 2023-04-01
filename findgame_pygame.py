from tkinter import messagebox, Tk
import pygame
import sys

width = 500
height = 500

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pathfinding App")

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        window.fill('grey22')

        pygame.display.flip()

main()

pygame.display.update()
