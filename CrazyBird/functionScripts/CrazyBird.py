#Comments by Simie Korgay
import pygame # type: ignore
import logging
import sys
import os
try:
    import Instructions
    logging.info("Instructions module imported successfully.")
    import GameplaySession
    logging.info("GameplaySession module imported successfully.")
    from ScoreBoard import Show
    logging.info("ScoreBoard module imported successfully.")
except Exception as Arguement:
    logging.exception("Error importing module(s). Please ensure the path is correct.")

#Checking if pygame is initialized, if not, initialize it
if pygame.get_init() == False:
    pygame.init()

#Setting up the screen attributes and dimmensions for menu
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Crazy Bird")

font = pygame.font.SysFont(None, 88)
title = font.render("Crazy Bird",True,(255, 255, 255))
fontOptions = pygame.font.SysFont(None, 28)
menu = {"PLAY": fontOptions.render("Press (SPACE) to START", True, (255, 255, 255)),
        "INSTUCTIONS": fontOptions.render("Press (i) to LEARN HOW TO PLAY", True, (255, 255, 255)),
        "SCORES": fontOptions.render("Press (s) to VIEW SCORES", True, (255, 255, 255)),
        "EXIT": fontOptions.render("Press (esc) to EXIT", True, (255, 255, 255))}
#Game loop elements and functionality
SKY_BLUE = (135, 206, 235)

SessionRunning = True
while SessionRunning:
    screen.fill(SKY_BLUE)
    screen.blit(title, (40, 30))
    x_offset = 15
    y_offset = 150
    for key, value in menu.items():
        screen.blit(value, (x_offset, y_offset))
        y_offset += 50
    pygame.display.update()
#Setting conditions for scenarios of the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            SessionRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_i:
                logging.info("Displaying instructions.")
                Instructions.explain("Instuctions")
            elif event.key == pygame.K_s:
                logging.info("Scores being displayed.")
                Show()
            elif event.key == pygame.K_SPACE:
                logging.info("Start game functionality not implemented yet.")  
                GameplaySession.Play()
            elif event.key == pygame.K_ESCAPE:
                logging.info("Game session terminated by user, exiting program")
                SessionRunning = False

pygame.quit()
sys.exit()