import pygame
import random

from square import Square
from player import Player
from ball import Ball
pygame.init()

WIDTH = 800
HEIGHT = 600
FPS = 60

clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

running = True

SPACE_BOXES = HEIGHT/2

player = Player(WIDTH, HEIGHT)
ball = Ball(player)
square = Square()
count = 0
cord_ball = []
cord_square = []
y = []
losing_texts = ["C'est pas mauvais, c'est très mauvais", "C'est pas moi, ça lag", "Un jour je serai.. le meilleur joueur", "T'es mauvais Jack"]
losing_text = random.choice(losing_texts)
winning_texts = ["T'es peut-être pas si mauvais que ça", "Winning is not everything, it's the only thing", "Tu es officiellement meilleur que le développeur"]
winning_text = random.choice(winning_texts)
for i in range(square.nt):
    for y in range(square.ny):
        for x in range(square.nx):
            new_square = Square()
            new_square.rect.x = square.rect.x
            new_square.rect.y = square.rect.y

            square.rect.x += square.rect.width + (WIDTH/square.nx - square.width)

            square.all_squares.add(new_square)
            if i == 0:
                new_square.life = 3
            elif i == 1:
                new_square.life = 2
            else:
                new_square.life = 1
        square.rect.y += square.rect.height + (SPACE_BOXES/(square.nt*square.ny) - square.height)
        square.rect.x = 10

losing = False
font = pygame.font.SysFont('Comic Sans MS', 30)
start_game = True
launch_counter = False
winning = False
end_game = False
while running:
    if not start_game:
        if len(square.all_squares) == 0:
            winning = True
            end_game = True
            continue
        square.pos_x = 0
        square.pos_y = 10
        pygame.display.set_caption(f"BREAK BRICKS (FPS : {int(clock.get_fps())})")
        screen.fill(pygame.Color("BEIGE"))
        clock.tick(FPS)
        if player.rect.x + player.width < 0:
            player.rect.x = WIDTH + player.width
        if player.rect.x - player.width > WIDTH:
            player.rect.x = 0 - player.width
        if player.number_of_lives == 0:
            losing = True
            end_game = True
        if not losing and not winning:
            ball.move(WIDTH, HEIGHT)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                player.rect.x -= player.speed

            if keys[pygame.K_RIGHT]:
                player.rect.x += player.speed
        screen.blit(player.image, player.rect)
        b = pygame.draw.circle(screen, pygame.Color("BLUE"), (ball.rect_x, ball.rect_y), ball.radius)
        life_bar = pygame.draw.rect(screen, pygame.Color("GREEN"), (player.rect.x, player.rect.y - 10, player.life_bar_width, player.life_bar_height))
        for s in square.all_squares:
            if s.life > 0:
                s.update_color()
                screen.blit(s.image, s.rect)
                s.image.fill(pygame.Color(s.color))
                if s.rect.colliderect(b):
                    ball.dy = -ball.dy
                    s.life -= 1
                square.rect.x += square.width + 25
            else:
                s.kill()
        if player.rect.colliderect(b):
            ball.speed += 0.05
            ball.dy = -ball.dy
        if end_game:
            if not launch_counter:
                launch_counter = True
                start_ticks = pygame.time.get_ticks()
            if losing:
                text = font.render(losing_text, False, pygame.Color("BLACK"))
            if winning:
                text = font.render(winning_text, False, pygame.Color("BLACK"))
            text_rect = text.get_rect()
            text_rect.center = (WIDTH/2, HEIGHT/2)
            screen.blit(text, (text_rect))
            scds = (pygame.time.get_ticks() - start_ticks) / 1000
            if scds >= 3:
                running = False
                pygame.quit()

    if start_game:
        screen.fill(pygame.Color("BLACK"))
        text = font.render("Appuyez sur ESPACE pour commencer", False, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (WIDTH / 2, HEIGHT / 2)
        screen.blit(text, text_rect)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if start_game:
                if event.key == pygame.K_SPACE:
                    start_game = False
            if event.key == pygame.K_DOLLAR:
                end_game = True
                winning = True
