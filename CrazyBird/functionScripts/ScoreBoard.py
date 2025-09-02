import pygame
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
database_path = os.path.join(os.path.dirname(current_dir), 'scoreDatabase')

sys.path.append(database_path)

import databaseConfig

def Show():
    databaseConfig.DB_initialization()
    if not pygame.get_init():
        pygame.init()

    SCREEN_WIDTH = 400
    SCREEN_HEIGHT = 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Crazy Bird")

    font = pygame.font.SysFont(None, 48)
    title = font.render("HIGHEST SCORES", True, (255, 255, 255))
    font1 = pygame.font.SysFont(None, 38)
    font2 = pygame.font.SysFont(None, 30)
    
    returnHome = font2.render("Return(Space)", True, (255, 255, 255))

    scores = databaseConfig.DB_show_scores()

    BLUE_SKY = (135, 206, 235)
    ScoreRunning = True
    while ScoreRunning:
        screen.fill(BLUE_SKY)
        
        y_offset = 30
        x_offset = 15
        
        screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, y_offset))
        y_offset += 70
        
        headers = ["Player", "Score", "Time"]
        for i, header in enumerate(headers):
            header_text = font1.render(header, True, (255, 255, 255))
            screen.blit(header_text, (x_offset + (i * 130), y_offset))
        y_offset += 40
        
        for i, score in enumerate(scores):
            if i >= 8:
                break
                
            player_id = score[0] if len(score[0]) <= 10 else score[0][:8] + "..."
            player_text = font2.render(player_id, True, (255, 255, 255))
            screen.blit(player_text, (x_offset, y_offset))
            
            score_text = font2.render(str(score[1]), True, (255, 255, 255))
            screen.blit(score_text, (x_offset + 130, y_offset))
            
            time_str = str(score[2])
            if " " in time_str:
                time_str = time_str.split()[1]
                time_str = time_str.rsplit(':', 1)[0]
                
            time_text = font2.render(time_str, True, (255, 255, 255))
            screen.blit(time_text, (x_offset + 260, y_offset))
            
            y_offset += 40
        
        screen.blit(returnHome, (x_offset, SCREEN_HEIGHT - 50))
        
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ScoreRunning = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    ScoreRunning = False