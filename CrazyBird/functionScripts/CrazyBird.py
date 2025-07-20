#Comments by Simie Korgay
import pygame # type: ignore
import logging
import sys
import os
try:
    import Instructions
    logging.info("Instructions module imported successfully.")
except Exception as Arguement:
    logging.exception("Error importing Instructions module. Please ensure the path is correct.")

#Checking if pygame is initialized, if not, initialize it
if pygame.get_init() == False:
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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_i:
                logging.info("Displaying instructions.")
                Instructions.explain("Instuctions")
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                #PLACEHOLDER FOR SCORE FUNCTIONALITY
                logging.info("Score functionality not implemented yet.")
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                #PLACEHOLDER FOR START GAME FUNCTIONALITY
                logging.info("Start game functionality not implemented yet.")  
#further 

pygame.quit()
sys.exit()