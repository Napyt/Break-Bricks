import pygame
pygame.init()


class Square(pygame.sprite.Sprite):
    def __init__(self):
        super(Square, self).__init__()
        self.life = 3
        self.color = "WHITE"
        self.width = 100
        self.height = 25
        self.nx = 6
        self.ny = 2
        self.nt = 3
        self.all_squares = pygame.sprite.Group()
        self.image = pygame.Surface([100, 25])
        self.image.fill(pygame.Color(self.color))
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 10

    def update_color(self):
        if self.life == 3:
            self.color = "BLACK"
        elif self.life == 2:
            self.color = "RED"
        elif self.life == 1:
            self.color = "GREEN"
