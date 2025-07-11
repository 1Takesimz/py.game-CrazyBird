#Comments by Simie Korgay
from sched import Event
import pygame # type: ignore
import sys

pygame.init()

#Setting up the screen attributes and dimmensions for menu
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Crazy Bird")

font = pygame.font.SysFont(None, 48)
title = font.render("Crazy Bird",True,(255, 255, 255))


#Game loop elements and functionality
SKY_BLUE = (135, 206, 235)


SessionRunning = True
while SessionRunning:
    screen.fill(SKY_BLUE)
    screen.blit(title, (100, 100))
    pygame.display.update()
#Setting conditions for scenarios of the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            SessionRunning = False
#further 

pygame.quit()
sys.exit()