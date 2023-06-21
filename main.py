import pygame
from gameScreen import GameScreen

pygame.init()
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
screen.fill('black')
timer = pygame.time.Clock()
fps = 30
pygame.display.set_caption("Container Pre-Marshalling Game")

def run_game():
    scene = GameScreen(screen)
    running = True
    while running:
        timer.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            scene.handle_event(event)
            scene.draw(screen)

        pygame.display.flip()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_game()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
