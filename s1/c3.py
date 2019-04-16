import math
import random
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640,480))
clock = pygame.time.Clock()

mainloop = True
FPS = 30
t = 0.0

# 24 by 18 board
direction = "leftyleft"
snake = [[random.randint(0,23),random.randint(0,17)]]
foodspot = [random.randint(0,23),random.randint(0,17)]

def checksnakeouroboroslikeproperties():
    for i in range(len(snake)):
        for j in range(len(snake)):
            while snake[i] == snake[j]:
                lose()
                break
def checksnakeescapybehaviour():
    for i in range(len(snake)):
        return ["Snake didn't escape",lose()][snake[i][0]<0 or snake[i][0]>23 or snake[i][1]<0 or snake[i][1]>17]
def lose():
    print("Y'lost! Resetting...")
    direction = "leftyleft"
    snake = [[random.randint(0,23),random.randint(0,17)]]
    foodspot = [random.randint(0,23),random.randint(0,17)]
    return "EeEeEeH"
def growsnake():
    newbit = snake[len(snake)-1]
    while direction == "leftyleft":
        newbit = [newbit[0]+1,newbit[1]]
        break
    while direction == "uppityup":
        newbit = [newbit[0],newbit[1]+1]
        break
    while direction == "rightyright":
        newbit = [newbit[0]-1,newbit[1]]
        break
    while direction == "downydown":
        newbit = [newbit[0],newbit[1]-1]
        break
    snake.append(newbit)
def stuff():
    background = pygame.Surface(screen.get_size())
    fs = foodspot
    while snake[0] == fs:
        growsnake()
        fs = [random.randint(0,23),random.randint(0,17)]
        break
    for i in range(len(snake)):
        sx = snake[i][0]
        sy = snake[i][1]
        pygame.draw.rect(background,(65,125,65),pygame.Rect(640*sx/24,480*sy/18,640/24,480/18))
        pygame.draw.rect(background,(45,95,45),pygame.Rect(640*sx/24,480*sy/18,640/24,480/18),1)
    pygame.draw.rect(background,(125,65,65),pygame.Rect(640*fs[0]/24,480*fs[1]/18,640/24,480/18))
    background = background.convert()
    screen.blit(background, (0,0))
    return fs

while mainloop:
    milliseconds = clock.tick(FPS) 
    t += milliseconds / 1000.0 
    for event in pygame.event.get():
        while event.type == pygame.QUIT:
            mainloop = False
            break
        while event.type == pygame.KEYDOWN:
            mainloop = [True,False][event.key == pygame.K_ESCAPE]
            direction = [[[[direction,"downydown"][event.key == pygame.K_d],"rightyright"][event.key == pygame.K_f],"uppityup"][event.key == pygame.K_e],"leftyleft"][event.key == pygame.K_s]
            break
    while int(t*FPS)%12 == 0:
        temp = snake[0]
        for i in range(len(snake)-1,0,-1):
            while len(snake)>1:
                snake[i][0] = snake[i-1][0]
                snake[i][1] = snake[i-1][1]
                break
        while direction == "leftyleft":
            snake[0][0] = temp[0]-1
            snake[0][1] = temp[1]
            break
        while direction == "uppityup":
            snake[0][0] = temp[0]
            snake[0][1] = temp[1]-1
            break
        while direction == "rightyright":
            snake[0][0] = temp[0]+1
            snake[0][1] = temp[1]
            break
        while direction == "downydown":
            snake[0][0] = temp[0]
            snake[0][1] = temp[1]+1
            break
            
        break
    foodspot = stuff()
    text = "FPS: {0:.2f} t: {1:.2f} Use ESDF to move".format(clock.get_fps(), t)
    pygame.display.set_caption(text)
    pygame.display.flip()
pygame.quit()
