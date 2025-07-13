import pygame

def explain(instructions):
    if not pygame.get_init():
        pygame.init()

    SCREEN_WIDTH = 400
    SCREEN_HEIGHT = 600
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("Crazy Bird")

    font = pygame.font.SysFont(None, 48)
    title =  font.render(instructions, True, (255, 255, 255))
    Explanation = font.render("\nInstructions",True, (255, 255, 255))

    InstructionRunning = True
    while InstructionRunning:
        screen.fill((0, 0, 0))
        screen.blit(title, (100, 100))
        screen.blit(Explanation, (100, 100))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                InstructionRunning = False
            elif event.key == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    InstructionRunning = False


