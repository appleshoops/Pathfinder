from tkinter import messagebox
import pygame
import sys

width = 600
height = 600

columns = 30
rows = 30

square_width = width // columns
square_height = height // rows

green = (163, 247, 180)
red = (250, 145, 152)
white = (255, 255, 255)
grey = (156, 156, 156)
blue = (148, 171, 247)

grid = []
queue = []

class square:
    def __init__(self, i, j):
        self.x = i
        self.y = j
        self.start = False
        self.wall = False
        self.end = False
        self.queued = False
        self.visited = False
        self.neighbors = []
    def draw(self, win, colour):
        pygame.draw.rect(win, colour, (self.x * square_width, self.y * square_height, square_width - 2, square_height -2))
    def add_neighbors(self):
        if self.x > 0:
            self.neighbors.append(grid[self.x - 1][self.y])
        if self.x < columns - 1:
            self.neighbors.append(grid[self.x + 1][self.y])

for i in range(columns):
    arr = []
    for j in range(rows):
        arr.append(square(i, j))
    grid.append(arr)

for i in range(columns):
    for j in range(rows):
        grid[i][j].add_neighbors()

start_square = grid[0][0]
start_square.start = True
start_square.visited = True
queue.append(start_square)

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pathfinding App")

def main():
    begin_search = False
    target_square_set = False
    searching = True
    target_square = None

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
        if begin_search:
            if len(queue) and searching:
                current_square = queue.pop(0)
                current_square.visited = True
                if current_square == target_square:
                    searching = False
                    print("Found target square")
                else:
                    for neighbor in current_square.neighbors:
                        if not neighbor.queued and not neighbor.wall:
                            neighbor.queued = True
                            queue.append(neighbor)
            else:
                if searching:
                    messagebox().wm_withdraw() # type: ignore
                    messagebox.showinfo("No Solution", "No path found")
                    searching = False

        window.fill('grey22')

        for i in range(columns):
            for j in range(rows):
                square = grid[i][j]
                square.draw(window, "gray8")
                if square.start:
                    square.draw(window, green)
                if square.wall:
                    square.draw(window, red)
                if square.end:
                    square.draw(window, blue)

        pygame.display.flip()

main()

pygame.display.update()
