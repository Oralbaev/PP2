import pygame
from pygame.locals import *
import random

pygame.init()
clock = pygame.time.Clock()

#fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, 'black')


background = pygame.image.load("AnimatedStreet.png")
screen = pygame.display.set_mode((400, 600))

enemy_image = pygame.image.load("Enemy.png")
enemy_rect = enemy_image.get_rect()
enemy_rect.center = (random.randint(40, 360), 0)

coin = pygame.image.load("coin.png")
gold = pygame.image.load("goldapple.png")
coin_image = pygame.transform.scale(coin, (75, 75))
apple_image = pygame.transform.scale(gold, (75, 75))
coin_rect = coin_image.get_rect()
coin_rect.center = (random.randint(10, 315), random.randint(200, 485))

player_image = pygame.image.load("Player.png")
player_rect = player_image.get_rect()
player_rect.center = (160, 520)

enemy_velocity = 2
level = 1
score = 0
fps = 60
number = random.randint(1, 11)

while True:
    screen.blit(background, (0,0))
    
    #initial drawings
    render_score = font_small.render(f'SCORE: {score}', True, 'black')
    screen.blit(render_score, (290, 5))
    screen.blit(enemy_image, enemy_rect)
    screen.blit(player_image, player_rect)

    #random weight
    if number == 10:
        screen.blit(apple_image, coin_rect)
    elif number != 10:
        screen.blit(coin_image, coin_rect)
    print(number)

    #enemy logic
    enemy_rect.move_ip(0, enemy_velocity)
    if enemy_rect[1] >= 600:
        enemy_rect.center = (random.randint(40, 360), 0)

    #level changing
    if score > level * 10:
        level += 1
        enemy_velocity += 1


    #control
    key = pygame.key.get_pressed()
    if player_rect.left > 0:
        if key[K_LEFT]:
            player_rect.move_ip(-5, 0)
    if player_rect.right < 400:        
        if key[K_RIGHT]:
            player_rect.move_ip(5, 0)
    if player_rect.bottom < 600:
        if key[K_DOWN]:
            player_rect.move_ip(0, 5)
    if player_rect.top:
        if key[K_UP]:
            player_rect.move_ip(0, -5)

    #crash
    if player_rect.colliderect(enemy_rect):  # Check collision using rect coordinates
        while True:
            screen.blit(game_over, (30, 250))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

    #coin collecting
    if player_rect.colliderect(coin_rect):
        coin_rect.center = (random.randint(100, 315), random.randint(200, 485))
        if number == 10:    score += 10
        elif number != 10:  score += 1
        number = random.randint(1, 11)

        
    

    #game quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pygame.display.flip()
    clock.tick(fps)

















