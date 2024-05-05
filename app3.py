import pygame
import random
from random import choice
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


randXa = 0
randXb = 800
randYa = 0
randYb = 600


speed = 5
x_control = speed
y_control = speed

pontos = 0
fonte = pygame.font.SysFont('arial', 40, True, True)

snakelength = 5
snakelist = []

die = False
lvl1 = True
lvl1loop = True
lvl2loop = True
lvl2 = True
start = True



def increasesnake(snakelist):
    for XeY in snakelist:
        pygame.draw.rect(screen, (0, 255, 0), (XeY[0], XeY[1], snakesize, snakesize))

def restartGame():
    global pontos, snakelist, snakelength, x, y, headlist, die, speed, lvl1loop

    speed = 5
    pontos = 0
    snakelength = 5
    x = width/2
    y = height/2

    headlist = []
    snakelist = []
    die = False
    lvl1loop


def restartAll():
    global pontos, snakelist, snakelength, x, y, headlist, die, speed, obstaclerun, lvl1, lvl1loop, obstaclerun2, lvl2, begin

    speed = 5
    pontos = 0
    snakelength = 5
    x = width/2
    y = height/2

    headlist = []
    snakelist = []
    die = False
    obstaclerun = False
    obstaclerun2 = False
    lvl1 = True
    lvl1loop = True
    lvl2 = True
    begin = True

    print('working')

def initialScreen():
    global start
    screen.fill('white')
    startmessage = f'Press SPACE to begin'
    formatted_startmessage = fonte.render(startmessage, True, 'black')
    lvlmessage1 = f'Level 1: get 10 points for the next level'
    formatted_lvlmessage1 = fonte.render(lvlmessage1, True, 'purple')
    screen.blit(formatted_startmessage, (220, 250))
    screen.blit(formatted_lvlmessage1, (70, 160))
    if pygame.key.get_pressed()[K_SPACE]:
        start = False
    pygame.display.update()


def restartAndMessage():
    global begin
    die = True
    begin = True
    while die:
        screen.fill((255,255,255))
        screen.blit(formatted_gameOver,(100, height/2 - 90))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    die = False
                    restartAll()


def restartGameLvl3():
    global pontos, snakelist, snakelength, x, y, headlist, die, speed, lvl1loop

    speed = 5
    pontos = 0
    snakelength = 5
    x = 800
    y = 640

    headlist = []
    snakelist = []
    die = False
    lvl1loop

def buildObstacle():
   global randXa, randXb, randYa, x_m, y_m
   rect1 = pygame.draw.rect(screen, (0, 0, 255), (110, 80, 80, 500))
   rect2 = pygame.draw.rect(screen, (0, 0, 255), (660, 80, 80, 500))


   if snake.colliderect(rect1):
       restartAndMessage()
   if snake.colliderect(rect2):
       restartAndMessage()

   if apple.colliderect(rect1):
       x_m = random.randint(randXa, randXb)
       y_m = random.randint(randYa, randYb)

   if apple.colliderect(rect2):
       x_m = random.randint(randXa, randXb)
       y_m = random.randint(randYa, randYb)
        

       

def buildObstacle2():
   global randXa, randXb, randYa, rect1, rect2, x_m, snakelength, speed, y_m, rect3
   rect1 = pygame.draw.rect(screen, (255, 0, 255), (80, 80, 80, 500))
   rect2 = pygame.draw.rect(screen, (255, 0, 255), (360, 80, 80, 500))
   rect3 = pygame.draw.rect(screen, (255, 0, 255), (680, 80, 80, 500))
   

   if apple.colliderect(rect1):
       x_m = random.randint(randXa, randXb)
       y_m = random.randint(randYa, randYb)

   if apple.colliderect(rect2):
       x_m = random.randint(randXa, randXb)
       y_m = random.randint(randYa, randYb)

   if apple.colliderect(rect3):
       x_m = random.randint(randXa, randXb)
       y_m = random.randint(randYa, randYb)



   if snake.colliderect(rect1):
       restartAndMessage()
   if snake.colliderect(rect2):
       restartAndMessage()
   if snake.colliderect(rect3):
       restartAndMessage()

   if snake.colliderect(apple):
       x_m  = choice([i for i in range(0, 800) if i not in range(120, 710)])
       print(x_m)
       y_m = random.randint(randYa, randYb)


x_m = random.randint(randXa, randXb)
y_m = random.randint(randYa, randYb)



interact = True
obstaclerun = False
obstaclerun2 = False
begin = True


while True:

    #initial screen#
    while start:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        initialScreen()


    screen.fill('white')

    snake = pygame.draw.rect(screen, (0, 255, 0), (x, y, snakesize, snakesize))
  
    apple = pygame.draw.rect(screen, (255, 0, 0), (x_m, y_m, applesize, applesize))


    '''text-messages'''
    message = f'Points: {pontos}'
    lvlmessage2 = f'get 20 points and watchout for the obstacles'
    lvlmessage2b = f'press SPACE to continue'
    gameOverMessage = f'Game over, press SPACE to restart'
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


    #começa o proximo nivel, quando chega a n pontos

    if lvl1 == True:
        if pontos == 3:
            obstaclerun = True
            lvl1 = False
            restartGame()
        
        #começa o level 2      

    if obstaclerun == True:
        while lvl1loop:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        lvl1loop = False

            screen.fill('white')
            lvl1looptext = fonte.render(lvlmessage2, True, 'black')
            screen.blit(lvl1looptext, (10, 300))
            pygame.display.update()

        buildObstacle()

    if begin == True:
        if pontos == 10:
            lvl2 = False
            begin = False
            obstaclerun = False
            obstaclerun2 = True
            restartGameLvl3()
            #termina level1 e começa lvl3
           

    if obstaclerun2 == True:
        while lvl2loop:
            screen.fill('white')
            lvl1looptext = fonte.render(lvlmessage2, True, 'black')
            screen.blit(lvl1looptext, (10, 300))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        lvl2loop = False

        buildObstacle2()



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
            restartAndMessage()

    
    if snake.colliderect(apple):
        x_m = random.randint(randXa, randXb)
        y_m = random.randint(randYa, randYb)
        pontos = pontos + 1
        snakelength += 3
        speed += 0.2


    x += x_control
    y += y_control



    screen.blit(formatted_text, (0, 580))
    clock = pygame.time.Clock()
    clock.tick(60)
    pygame.display.update()