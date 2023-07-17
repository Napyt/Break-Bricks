import pygame
from player import Player
pygame.init()


class Ball(pygame.sprite.Sprite):
    def __init__(self, player):
        super(Ball, self).__init__()
        self.player = player
        self.speed = 2
        self.rect_x = self.player.rect.centerx
        self.rect_y = self.player.rect.centery - 30
        self.radius = 10
        self.dx = 1
        self.dy = 1

    def reset_pos(self):
        self.player.number_of_lives -= 1
        self.player.life_bar_width -= self.player.original_life_bar_width / 3
        self.rect_x = self.player.rect.centerx
        self.rect_y = self.player.rect.centery - 30

    def move(self, screen_width, screen_height):
        if self.rect_x - self.radius <= 0:
            self.dx = 1
        if self.rect_x + self.radius >= screen_width:
            self.dx = -1
        if self.rect_y + self.radius >= screen_height:
            self.reset_pos()
        if self.rect_y - self.radius <= 0:
            self.dy = 1

        self.rect_x += self.speed * self.dx
        self.rect_y += self.speed * self.dy



