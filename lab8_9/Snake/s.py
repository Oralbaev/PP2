import pygame
from random import randrange
import random


RES = 800
SIZE = 50
screen = pygame.display.set_mode([RES, RES])
appleCrd = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
fps = 3
length = 2
x, y = 50, 50
snake = [(x, y)]
dx, dy = 0, 0
score = 0
level = 1

number = random.randint(1, 11)
start_time = pygame.time.get_ticks()

pygame.init()
clock = pygame.time.Clock()

image = pygame.image.load("apple.png").convert()
image2 = pygame.image.load('head.png').convert()
image3 = pygame.image.load('goldapple.png').convert()
new_size = (50, 50)
apple = pygame.transform.scale(image, new_size)
head = pygame.transform.scale(image2, new_size)
goldenApple = pygame.transform.scale(image3, new_size)

font_score = pygame.font.SysFont('Arial', 26, bold=True)
font_end = pygame.font.SysFont('Arial', 60, bold=True)

while True:
    screen.fill((0, 0, 0))
    
    
    #control
    key = pygame.key.get_pressed()
    if key[pygame.K_w] and dy != 1:
        dx, dy = 0, -1
    if key[pygame.K_s] and dy != -1:
        dx, dy = 0, 1
    if key[pygame.K_a] and dx != 1:
        dx, dy = -1, 0
    if key[pygame.K_d] and dx != -1:
        dx, dy = 1, 0

    #apple disappearing
    if (pygame.time.get_ticks() - start_time) / 1000 >= 10:
        appleCrd = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
        number = random.randint(1, 10)
        start_time = pygame.time.get_ticks()

    #drawing snake, apple
    for i, j in snake[0:len(snake) - 1]:
        pygame.draw.rect(screen, pygame.Color('green'), (i, j, SIZE - 1, SIZE - 1))
    screen.blit(head, snake[-1])

    if number < 10:
        screen.blit(apple, appleCrd)
    elif number == 10: screen.blit(goldenApple, appleCrd)
    
    #move snake
    x += 50 * dx
    y += 50 * dy
    snake.append((x,y))
    snake = snake[-length:]

    #eating apple
    if snake[-1] == appleCrd and number < 7:
        appleCrd = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
        length += 1
        score += 1
        number = random.randint(1, 10)
        start_time = pygame.time.get_ticks()
    elif snake[-1] == appleCrd and number > 7:
        appleCrd = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
        length += 3
        score += 3
        number = random.randint(1, 10)
        start_time = pygame.time.get_ticks()

    #show score
    render_score = font_score.render(f'SCORE: {score}', 1, pygame.Color('orange'))
    render_level = font_score.render(f'LEVEL: {level}', 1, pygame.Color('orange'))
    screen.blit(render_score, (5, 5))
    screen.blit(render_level, (150, 5))

    #level changing
    if score > 2 ** level:
        level += 1
        fps += 1

    #game over
    if snake[-1] in snake[0:len(snake) - 2] or x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE:
        while True:
            render_end = font_end.render("GAME OVER", 1, pygame.Color('orange'))
            screen.blit(render_end, (RES // 2 - 170, RES // 3))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()








    #game quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pygame.display.flip()
    clock.tick(fps)

    
    