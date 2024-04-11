import pygame
from random import randrange

RES = 800
SIZE = 50

x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
length = 2
snake = [(x, y)]
dx, dy = 0, 0
fps = 1
score = 0

pygame.init()
sc = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()

font_score = pygame.font.SysFont('Arial', 26, bold=True)
font_end = pygame.font.SysFont('Arial', 60, bold=True)

image = pygame.image.load('apple.png').convert()
h = pygame.image.load('head.png').convert()
new_size = (50, 50)
resized_image = pygame.transform.scale(image, new_size)
head = pygame.transform.scale(h, new_size)

while True:
    sc.fill(pygame.Color('black'))
    
    #drawing snake, apple
    [(pygame.draw.rect(sc, pygame.Color('green'), (i, j, SIZE - 1, SIZE - 1))) for i, j in snake[0:len(snake) - 1]]
    sc.blit(resized_image, apple)
    sc.blit(head, snake[-1])

    #show score
    render_score = font_score.render(f'SCORE: {score}', 1, pygame.Color('orange'))
    sc.blit(render_score, (5, 5))

    #snake moving
    x += dx * SIZE
    y += dy * SIZE
    snake.append((x, y))
    snake = snake[-length:]

    #eating apple
    if snake[-1] == apple:
        apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
        length += 1

    #game over
    if snake[-2] in snake[0:len(snake) - 2] or x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE:
        while True:
            render_end = font_end.render("GAME OVER", 1, pygame.Color('orange'))
            sc.blit(render_end, (RES // 2 - 170, RES // 3))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()



    pygame.display.flip()
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


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


