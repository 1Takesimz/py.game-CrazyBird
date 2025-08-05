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
    instructionText = {"Title": font1.render("HOW TO PLAY:",True, (255, 255, 255)),
                       "first_line": font1.render("Press SPACEBAR in order",True, (255, 255, 255)),
                       "second_line": font1.render("manevour inbeteen incoming",True, (255, 255, 255)),
                       "third_line": font1.render("pipes to add to your score",True, (255, 255, 255)),
                       "fourth_line": font1.render("Good luck and happy flying :)",True, (255, 255, 255))}

    font2 = pygame.font.SysFont(None, 30)
    returnHome = font2.render("Return(Space)",True, (255, 255, 255))
    InstructionRunning = True
    while InstructionRunning:
        y_offset = 100
        x_offset = 15
        screen.blit(instructionText["Title"], (x_offset, y_offset))
        y_offset += 50
        screen.blit(instructionText["first_line"], (x_offset, y_offset))
        y_offset += 50
        screen.blit(instructionText["second_line"], (x_offset, y_offset))
        y_offset += 50
        screen.blit(instructionText["third_line"], (x_offset, y_offset))
        y_offset += 50
        screen.blit(instructionText["fourth_line"], (x_offset, y_offset))
        y_offset += 250
        screen.blit(returnHome, (x_offset, y_offset))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    InstructionRunning = False