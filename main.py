import pygame
from startScreen import StartScreen
from gameScreen import GameScreen
from endScreen import EndScreen

scenes = {'Start': StartScreen(),
          'Game': GameScreen(),
          'End': EndScreen()}

def run_game():
    scene = scenes['Start']
    pygame.init()
    SCREEN_WIDTH = 1200
    SCREEN_HEIGHT = 800
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    screen.fill('black')
    timer = pygame.time.Clock()
    fps = 30
    pygame.display.set_caption("Overstow Cleanup")
    running = True
    while running:
        timer.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            # new_scene = scene.handleEvent(event)
            # scene.draw(screen)
            # scene = new_scene


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_game()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
