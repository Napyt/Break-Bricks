import pygame
pygame.init()


class Player(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super(Player, self).__init__()
        self.speed = 3
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.height = 10
        self.width = 75
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(pygame.Color("BLUE"))
        self.rect = self.image.get_rect()
        self.rect.center = (self.screen_width//2, self.screen_height - self.height - 10)
        self.original_life_bar_width = self.width
        self.life_bar_width = self.original_life_bar_width
        self.life_bar_height = self.height/2
        self.number_of_lives = 3
    """"
    def reset_game(self, square, WIDTH, HEIGHT, SPACE_BOXES):
        self.rect.center = (self.screen_width // 2, self.screen_height - self.height - 10)
        for i in range(square.nt):
            for y in range(square.ny):
                for x in range(square.nx):
                    new_square = square
                    new_square.rect.x = square.rect.x
                    new_square.rect.y = square.rect.y

                    square.rect.x += square.rect.width + (WIDTH / square.nx - square.width)

                    square.all_squares.add(new_square)
                    if i == 0:
                        new_square.life = 3
                    elif i == 1:
                        new_square.life = 2
                    else:
                        new_square.life = 1
                square.rect.y += square.rect.height + (SPACE_BOXES / (square.nt * square.ny) - square.height)
                square.rect.x = 10

        self.life_bar_width = self.original_life_bar_width
        self.number_of_lives = 3
        """