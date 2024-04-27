import pygame
import random
from pygame.locals import *
from sys import exit

pygame.init()

width = 840
height = 640


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

snakelength = 5
snakelist = []

die = False
lvl1 = True
lvl1begin = False
start = True
obstaclerun = False
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



def buildobstacles():
    global obstacle
    obstaclex = 50
    obstacley = 100
    obsizex = 50
    obsizey = 100

    obstacle = pygame.draw.rect(screen, (0, 0, 255), (obstaclex, obstacley, obsizex, obsizey))


while True:

    while start:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        screen.fill('white')
        startmessage = f'Press \'c\' to begin'
        formatted_startmessage = fonte.render(startmessage, True, 'black')
        screen.blit(formatted_startmessage, (220, 220))
        if pygame.key.get_pressed()[K_c]:
            start = False
        pygame.display.update()


    screen.fill('white')
    snake = pygame.draw.rect(screen, (0, 255, 0), (x, y, snakesize, snakesize))
    apple = pygame.draw.rect(screen, (255, 0, 0), (x_m, y_m, applesize, applesize))


    '''text-messages'''
    message = f'Pontos: {pontos}'
    lvlmessage1 = f'Get 15 points'
    lvlmessage2 = f'get 20 points, watchout the obstacles'
    lvlmessage2b = f'press c to continue'
    formatted_lvlmessage2 = fonte.render(lvlmessage2, True, 'black')
    formatted_lvlmessage2b = fonte.render(lvlmessage2b, True, 'black')
    formatted_lvlmessage1 = fonte.render(lvlmessage1, True, 'black')
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

    if pontos >= 5:
        while lvl1:
            screen.fill('white')
            screen.blit(formatted_lvlmessage2, (100, 200))
            screen.blit(formatted_lvlmessage2b, (100, 100))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
            pygame.display.update()
            if pygame.key.get_pressed()[K_c]:
                lvl1 = False
                lvl1begin = True
                obstaclerun = True

        if lvl1begin == True:
            speed = 5
            pontos = 0
            snakelength = 5
            x = width / 2
            y = height / 2

            headlist = []
            snakelist = []
            lvl1begin = False

    if obstaclerun == True:
        buildobstacles()

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
    print(headlist)

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
                        obstaclerun = False
                        lvl1begin = True
            pygame.display.update()

    if snake.colliderect(apple):
        x_m = random.randint(0, 800)
        y_m = random.randint(0, 600)
        pontos = pontos + 1
        snakelength += 3
        speed += 0.2


    x += x_control
    y += y_control




    screen.blit(formatted_text, (0, 500))
    clock = pygame.time.Clock()
    clock.tick(60)
    pygame.display.update()