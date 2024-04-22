import pygame
import random
from pygame.locals import *
from sys import exit

pygame.init()

width = 840
height = 640

hitsound = pygame.mixer.Sound('hitsound2.wav')
hitsound.set_volume(0.1)
pygame.mixer.music.set_volume(0.1)

pygame.display.set_caption('TesteJogo')

screen = pygame.display.set_mode((width, height))

x=420
y=320

snakesize = 30
applesize = 30

x_m = random.randint(0, 800)
y_m = random.randint(0, 600)

speed = 5
x_control = speed
y_control = speed

pontos = 0
fonte = pygame.font.SysFont('arial', 40, True, True)

snakelength = 40
snakelist = []

die = False
def increasesnake(snakelist):
    for XeY in snakelist:
        pygame.draw.rect(screen, (0, 255, 0), (XeY[0], XeY[1], snakesize, snakesize))

def restartGame():
    global pontos, snakelist, snakelength, x, y, headlist, die, speed

    speed = 5
    pontos = 0
    snakelength = 5
    x = width/2
    y = height/2

    headlist = []
    snakelist = []
    die = False

while True:

    start = True

    while start:
        screen.fill('white')
        startmessage = f'Aperte qualquer botao para inciar'
        formatted_startmessage = fonte.render(startmessage, True, 'black')
        screen.blit(formatted_startmessage, (100, 200))
        if pygame.key.get_pressed()[K_c]:
            start = False
        pygame.display.update()


    screen.fill('white')
    snake = pygame.draw.rect(screen, (0, 255, 0), (x, y, snakesize, snakesize))
    apple = pygame.draw.rect(screen, (255, 0, 0), (x_m, y_m, applesize, applesize))

    message = f'Pontos: {pontos}'
    gameOverMessage = f'Você perdeu, aperte \'r\' para reiniciar'
    formatted_gameOver = fonte.render(gameOverMessage, True, 'black')
    formatted_text = fonte.render(message, True, 'black')
    increasesnake(snakelist)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if pygame.key.get_pressed()[K_d]:
            if x_control == -speed:
                pass
            else:
                x_control = speed
                y_control = 0
        if pygame.key.get_pressed()[K_a]:
            if x_control == speed:
                pass
            else:
                x_control = -speed
                y_control = 0
        if pygame.key.get_pressed()[K_w]:
            if y_control == speed:
                pass
            else:
                y_control = -speed
                x_control = 0
        if pygame.key.get_pressed()[K_s]:
            if y_control == -speed:
                pass
            else:
                y_control = speed
                x_control = 0



    if x > width:
        x = 0
    if x < -40:
        x = width - 40
    if y < -40:
        y = height - 40
    if y > height:
        y =  0




    if len(snakelist) > snakelength:
            del snakelist[0]

    headlist = []
    headlist.append(x)
    headlist.append(y)
    snakelist.append(headlist)

    '''se a cobra colidir em si mesma'''

    if snakelist.count(headlist) > 1:
        die = True
        while die:
            screen.fill((255,255,255))
            screen.blit(formatted_gameOver,(100, height/2 - 90))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        restartGame()
            pygame.display.update()

    if snake.colliderect(apple):
        x_m = random.randint(0, 800)
        y_m = random.randint(0, 600)
        pontos = pontos + 1
        hitsound.play()
        snakelength += 3
        speed += 0.2


    x += x_control
    y += y_control

    screen.blit(formatted_text, (0, 500))
    clock = pygame.time.Clock()
    clock.tick(60)
    pygame.display.update()