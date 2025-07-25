
import pygame  # type: ignore   
import os

import pygame.display
def Play():
    if not pygame.get_init():
        pygame.init()

    SCREEN_WIDTH = 400
    SCREEN_HEIGHT = 600
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("Crazy Bird")


    font = pygame.font.SysFont(None, 38)
    pause_text = {
        "Pause" : font.render("PAUSED", True, (255, 255, 255)),
        "PauseExit": font.render("Press X to exit", True, (255, 255, 255)),
        "PauseRestart": font.render("Press R to restart", True, (255, 255, 255)),
        "PauseContinue": font.render("Press C to continue", True, (255, 255, 255))
        }
    score = 0
    SCORE_font = pygame.font.SysFont(None, 48)

    clock = pygame.time.Clock()
    FPS = 60
    gravity = 0.25
    bird_movement = 0
    game_active = True
    paused = False

    bird_react = pygame.Rect(100, 250, 30, 50) 

    pipes = []
    pipe_frequency = 1500  # milliseconds
    pipe_gap = 150
    pipe_Width = 60
    last_pipe = pygame.time.get_ticks()

    SCORE_surface = SCORE_font.render(f"Score: {int(score)}", True, (255, 255, 255))
    screen.blit(SCORE_surface, (100,100))
    pygame.display.update()

    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game_active:
                    bird_movement = -7
                elif event.key == pygame.K_r and not game_active:
                    game_active = True
                    pipes.clear()
                    bird_react.y = 250
                    bird_movement = 0
                    score = 0
                elif event.key == pygame.K_p:
                    paused = not paused 
                    game_active = False
                    

        if game_active and not paused:
            bird_movement += gravity
            bird_react.y += bird_movement

        if game_active:
            screen.fill((0,0,0))
            pygame.draw.rect(screen, (255, 255, 0), bird_react)
            for pipe in pipes:
                pygame.draw.rect(screen, (0, 255, 0), pipe)

            score_surface = SCORE_font.render(f"Score: {int(score)}", True, (255, 255, 255))
            screen.blit(score_surface, (10, 10))
                
        if paused:
            y_offset = 100
            x_offset = 50
            screen.blit(pause_text["Pause"], (x_offset, y_offset))
            y_offset += 50
            screen.blit(pause_text["PauseExit"], (x_offset, y_offset))
            y_offset += 50
            screen.blit(pause_text["PauseRestart"], (x_offset, y_offset))
            y_offset += 50
            screen.blit(pause_text["PauseContinue"], (x_offset, y_offset))
            pygame.display.update()
            
                  

