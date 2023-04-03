import pygame
import os
import random
import sys

pygame.init()

screenHeight = 600
screenWidth = 1100
screen = pygame.display.set_mode((screenWidth, screenHeight))

running = [pygame.image.load(os.path.join("Assets/Sonic", "SonicRun1.png")),
           pygame.image.load(os.path.join("Assets/Sonic", "SonicRun2.png"))]
jumping = pygame.image.load(os.path.join("Assets/Sonic", "SonicJump.png"))

hazard = [pygame.image.load(os.path.join("Assets/Hazards", "Enemy1.png"))]

font = pygame.font.SysFont("arial", 50, True)

class Character:
    xPos = 80
    yPos = 210
    jumpVel = 8.5

    def __init__(self, img=running[0]):
        self.img = img
        self.character_run = True
        self.character_jump = False
        self.jumpVel = self.jumpVel
        self.rect = pygame.Rect(self.xPos, self.yPos, img.get_width(), img.get_height())
        self.step_index = 0
    
    def update(self):
        if self.character_run:
            self.run()
        if self.character_jump:
            self.jump()
        if self.step_index >= 10:
            self.step_index = 0

    def jump(self):
        self.image = jumping
        if self.character_jump:
            self.rect.y = self.jump_vel * 4  # type: ignore
            self.jump_vel -= 0.8
        if self.jump_vel <= -self.jump_vel: # type: ignore
            self.dino_jump = False
            self.dino_run = True
            self.jump_vel = self.jump_vel
    def run(self):
        self.image = running[self.step_index // 5]
        self.rect.x = self.xPos
        self.rect.y = self.yPos
        self.step_index += 1

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))




def main():
    global game_speed, xpos_bg, xpos_bg2, score
    points = 0
    clock = pygame.time.Clock()

    characters = [Character()]

    xpos_bg = 0
    ypos_bg = 380
    game_speed = 30

    def score():
        global points, game_speed
        points = 0
        points += 1
        if points % 100 == 0:
            game_speed += 1
        text = font.render(f'Points:  {str(points)}', True, (0, 0, 0))
        font.render(f'Points:  {str(points)}', True, (0, 0, 0))


    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((255, 255, 255))

        for character in characters:
            character.update()
            character.draw(screen)

        pressed = pygame.key.get_pressed()

        for i, character in enumerate(characters):
            if pressed[pygame.K_SPACE]:
                character.character_jump = True
                character.character_run = False

        score()
        clock.tick(30)
        pygame.display.update()

main()