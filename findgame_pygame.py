import pyautogui
import pygame
import sys

width = 600
height = 600

window = pygame.display.set_mode((width, height))

columns = 30
rows = 30

square_width = width // columns
square_height = height // rows

green = (163, 247, 180)
red = (250, 145, 152)
white = (255, 255, 255)
grey = (156, 156, 156)
blue = (148, 171, 247)
pink = (252, 182, 238)
yellow = (241, 255, 184)

grid = []
queue = []
path = []

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
        self.prior = None
    def draw(self, win, colour):
        pygame.draw.rect(win, colour, (self.x * square_width, self.y * square_height, square_width - 2, square_height -2))
    def add_neighbors(self):
        if self.x > 0:
            self.neighbors.append(grid[self.x - 1][self.y])
        if self.x < columns - 1:
            self.neighbors.append(grid[self.x + 1][self.y])
        if self.y > 0:
            self.neighbors.append(grid[self.x][self.y - 1])
        if self.y < rows - 1:
            self.neighbors.append(grid[self.x][self.y + 1])

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

def main():
    
    begin_search = False
    end_square_set = False
    searching = True
    end_square = None

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
                if event.buttons[2] and not end_square_set:
                    i = x // square_width
                    j = y // square_height
                    end_square = grid[i][j]
                    end_square_set = True
                    end_square.end = True

            if [pygame.K_TAB] and end_square_set:
                begin_search = True
        if begin_search:
            if len(queue) and searching:
                current_square = queue.pop(0)
                current_square.visited = True
                if current_square == end_square:
                    searching = False
                    print("Found end square")
                    while current_square.prior != start_square:
                        path.append(current_square.prior)
                        current_square = current_square.prior
                else:
                    for neighbor in current_square.neighbors:
                        if not neighbor.queued and not neighbor.wall:
                            neighbor.queued = True
                            neighbor.prior = current_square
                            queue.append(neighbor)

        window.fill('grey22')

        for i in range(columns):
            for j in range(rows):
                square = grid[i][j]
                square.draw(window, "gray8")

                if square.queued:
                    square.draw(window, pink)
                if square.visited:
                    square.draw(window, white)

                if square in path:
                    square.draw(window, yellow)


                if square.start:
                    square.draw(window, green)
                if square.wall:
                    square.draw(window, red)
                if square.end:
                    square.draw(window, blue)

        pygame.display.flip()

main()

pygame.display.update()
