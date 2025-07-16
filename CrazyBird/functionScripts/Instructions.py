import pygame
import sys
import os

def explain(instructions):
    if not pygame.get_init():
        pygame.init()

    SCREEN_WIDTH = 400
    SCREEN_HEIGHT = 600
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("Crazy Bird")

    font = pygame.font.SysFont(None, 48)
    title =  font.render("INSTRUCTIONS", True, (255, 255, 255))
    font1 = pygame.font.SysFont(None, 38)
    Explanation1 = font1.render("HOW TO PLAY:",True, (255, 255, 255))
    Explanation2 = font1.render("Press SPACEBAR in order",True, (255, 255, 255))
    Explanation3 = font1.render("manevour inbeteen incoming",True, (255, 255, 255))
    Explanation4 = font1.render("pipes to add to your score",True, (255, 255, 255))
    Explanation5 = font1.render("Good luck and happy flying :)",True, (255, 255, 255))
    font2 = pygame.font.SysFont(None, 30)
    Explanation6 = font2.render("Return(Space)",True, (255, 255, 255))
    InstructionRunning = True
    while InstructionRunning:
        screen.fill((0, 0, 0))
        screen.blit(title, (70, 70))
        screen.blit(Explanation1, (20, 140))
        screen.blit(Explanation2, (20, 170))
        screen.blit(Explanation3, (20, 195))
        screen.blit(Explanation4, (20, 220))
        screen.blit(Explanation5, (15, 290))
        screen.blit(Explanation6, (20, 550))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                InstructionRunning = False


