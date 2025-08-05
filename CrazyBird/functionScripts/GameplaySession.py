import pygame  # type: ignore   
import os
import random
import logging
import pygame.display
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[logging.FileHandler('gameplay.log'), logging.StreamHandler()])
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
    SCORE_font = pygame.font.SysFont(None, 48)

    clock = pygame.time.Clock()
    FPS = 60
    gravity = 0.25
    bird_movement = 0
    game_active = True
    paused = False
    score = 0

    bird = pygame.Rect(100, 250, 30, 50) 

    pipes = []
    pipe_frequency = 1500  # milliseconds
    pipe_gap = 150
    pipe_width = 60
    last_pipe = pygame.time.get_ticks()

    def create_pipe():  
        height = random.randint(100, 400)
        top_pipe = pygame.Rect(SCREEN_WIDTH, 0, pipe_width, height - pipe_gap)
        bottom_pipe = pygame.Rect(SCREEN_WIDTH, height + pipe_gap, pipe_width, SCREEN_HEIGHT - height - pipe_gap)
        return top_pipe, bottom_pipe

    def move_pipes(pipes):  
        for pipe in pipes:
            pipe.x -= 5
        return [pipe for pipe in pipes if pipe.x > -pipe_width]

    def check_collision(bird, pipes):
        if bird.top <= 0 or bird.bottom >= SCREEN_HEIGHT:
            return True
        for pipe in pipes:
            if bird.colliderect(pipe):
                return True
        return False

    def score_display(score):
        score_surface = SCORE_font.render(f"Score: {int(score)}", True, (255, 255, 255))
        screen.blit(score_surface, (10, 10))
    
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p and game_active:
                    paused = not paused
                    logging.info(f"Game {'paused' if paused else 'resumed'}.")

                if paused:
                    try:
                        if event.key == pygame.K_x:
                            logging.info("Gameplay Session terminated exited by user.")
                            return False
                        elif event.key == pygame.K_r:
                            game_active = True
                            paused = False
                            pipes.clear()
                            bird.y = 250
                            bird_movement = 0
                            score = 0
                            logging.info("Game restarted.")
                            last_pipe = pygame.time.get_ticks()
                        elif event.key == pygame.K_c:
                            paused = False
                            logging.info("Game continued from paused state.")

                    except Exception as e:
                        logging.error(f"Error handling pause events in Gameplay.py: {e}") #PAUSED STATE

                elif game_active:
                    if event.key == pygame.K_SPACE:
                        bird_movement = -7 #ACTIVE STATE

                elif not game_active:
                    if event.key == pygame.K_SPACE and game_active:
                        bird_movement = -7
                    elif event.key == pygame.K_r:
                        game_active = True
                        pipes.clear()
                        bird.y = 250
                        bird_movement = 0
                        score = 0
                        last_pipe = pygame.time.get_ticks()   
                    elif event.key == pygame.K_x:
                        return False
                        logging.info("Gameplay Session terminated exited by user.")
                    elif event.key == pygame.K_s:
                        # Placeholder for score saving functionality
                        logging.info("Score saving functionality not implemented yet.")

        if game_active and not paused:
            bird_movement += gravity
            bird.y += bird_movement
            
            time = pygame.time.get_ticks()
            if time - last_pipe > pipe_frequency:
                pipes.extend(create_pipe())
                last_pipe = time
                score += 1

            pipes = move_pipes(pipes)

            if check_collision(bird, pipes):
                game_active = False
                logging.info("Collision detected. Game over.")

        screen.fill((135, 206, 235))

        if game_active:
            for pipe in pipes:
                pygame.draw.rect(screen, (0, 255, 0), pipe)
            pygame.draw.rect(screen, (255, 255, 0), bird)
            score_display(score) 

        elif paused:
            y_offset = 100
            x_offset = 50
            screen.blit(pause_text["Pause"], (x_offset, y_offset))
            y_offset += 50
            screen.blit(pause_text["PauseExit"], (x_offset, y_offset))
            y_offset += 50
            screen.blit(pause_text["PauseRestart"], (x_offset, y_offset))
            y_offset += 50
            screen.blit(pause_text["PauseContinue"], (x_offset, y_offset))

        elif not game_active and not paused:

            GameOver_text = {
        "GAMEOVER" : font.render("GAME OVER", True, (255, 255, 255)),
        "GameOver_Exit": font.render("Press X to exit", True, (255, 255, 255)),
        "GameOver_Restart": font.render("Press R to restart", True, (255, 255, 255)),
        "GameOver_Save_Score": font.render("Press S to save score now", True, (255, 255, 255))
        }          
            score_text = font.render(f"Final Score: {int(score)}", True, (255, 255, 255))
            screen.blit(score_text, (50, SCREEN_HEIGHT // 2 + 50))

            y_offset = 100
            x_offset = 50
            screen.blit(GameOver_text["GAMEOVER"], (x_offset, y_offset))
            y_offset += 50
            screen.blit(GameOver_text["GameOver_Exit"], (x_offset, y_offset))
            y_offset += 50
            screen.blit(GameOver_text["GameOver_Restart"], (x_offset, y_offset))
            y_offset += 50
            screen.blit(GameOver_text["GameOver_Save_Score"], (x_offset, y_offset))
        pygame.display.update()
