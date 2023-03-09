import pygame
from pygame.locals import *

pygame.init()

green = (163, 247, 180)
red = (250, 145, 152)
white = (255, 255, 255)
grey = (156, 156, 156)

window_size = (900, 900)
square_size = 30
num_rows = 20
num_cols = 20
grid = [[white for j in range(num_cols)] for i in range(num_rows)]

screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("A* Pathfinding App")
font = pygame.font.SysFont(None, 24)

draw_green = True

# Define the button rectangle
button_rect = pygame.Rect(window_size[0] - 70, 30, 60, 10)

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
                if button_rect.collidepoint(mouse_pos):
                    draw_green = not draw_green
                else:
                    row = mouse_pos[1] // square_size
                    col = mouse_pos[0] // square_size
                    if draw_green:
                        grid[row][col] = green
                    else:
                        grid[row][col] = grey
            # Check for right mouse button click
            elif event.button == 3:
                mouse_pos = pygame.mouse.get_pos()
                row = mouse_pos[1] // square_size
                col = mouse_pos[0] // square_size
                grid[row][col] = red

    # Clear the screen
    screen.fill(white)

    # Draw the button
    pygame.draw.rect(screen, white, button_rect, 2)
    if draw_green:
        button_text = font.render("Green", True, green)
    else:
        button_text = font.render("Grey", True, grey)
    screen.blit(button_text, (window_size[0] - 60, 107))

    # Draw the grid
    for row in range(num_rows):
        for col in range(num_cols):
            rect = pygame.Rect(col * square_size, row * square_size, square_size, square_size)
            pygame.draw.rect(screen, grid[row][col], rect)

    # Update the display
    pygame.display.update()
