import pygame


class StartScreen:
    def __init__(self, screen: pygame.Surface):
        self.font = pygame.font.Font(None, 100)
        self.play_button = self.font.render("PLAY", True, 'black')
        self.play_button_rect = self.play_button.get_rect()
        self.is_play_pressed = False

    def handle_event(self, event: pygame.event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("hi")
            if self.play_button_rect.collidepoint(event.pos):
                self.font = pygame.font.Font(None, 90)
                self.play_button = self.font.render("PLAY", True, 'black')
                self.play_button_rect = self.play_button.get_rect()
                self.is_play_pressed = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if self.is_play_pressed:
                self.font = pygame.font.Font(None, 100)
                self.play_button = self.font.render("PLAY", True, 'black')
                self.play_button_rect = self.play_button.get_rect()
                self.is_play_pressed = False
                return 'Game'
        return None

    def draw(self, screen: pygame.Surface):
        screen.fill('white')
        self.play_button_rect.left = (screen.get_width() - self.play_button_rect.width) // 2
        self.play_button_rect.top = (screen.get_height() - self.play_button_rect.height) // 2
        screen.blit(self.play_button, self.play_button_rect)
