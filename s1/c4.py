import random
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640,480))
clock = pygame.time.Clock()

mainloop = True
FPS = 30
t = 0.0

thefirstderivativeofpositionwithrespecttotime = 4
raindrops = [[random.randint(0,640),random.randint(0,480)],[random.randint(0,640),random.randint(0,480)],[random.randint(0,640),random.randint(0,480)],[random.randint(0,640),random.randint(0,480)],[random.randint(0,640),random.randint(0,480)],[random.randint(0,640),random.randint(0,480)],[random.randint(0,640),random.randint(0,480)],[random.randint(0,640),random.randint(0,480)],[random.randint(0,640),random.randint(0,480)],[random.randint(0,640),random.randint(0,480)],[random.randint(0,640),random.randint(0,480)],[random.randint(0,640),random.randint(0,480)],[random.randint(0,640),random.randint(0,480)],[random.randint(0,640),random.randint(0,480)],[random.randint(0,640),random.randint(0,480)],[random.randint(0,640),random.randint(0,480)],[random.randint(0,640),random.randint(0,480)],[random.randint(0,640),random.randint(0,480)],[random.randint(0,640),random.randint(0,480)],[random.randint(0,640),random.randint(0,480)]]
def drippity():
    for i in range(len(raindrops)):
        drop = raindrops[i]
        raindrops[i][1] = drop[1] + int(thefirstderivativeofpositionwithrespecttotime*drop[1])
def droppity():
    for i in range(len(raindrops)):
        drop = raindrops[i]
        raindrops[i] = [drop,[random.randint(0,640),random.randint(0,480)]][drop[1]>480]
    
def stuff():
    background = pygame.Surface(screen.get_size())
    drippity()
    droppity()
    #raindrops have properties
    pygame.draw.rect(background,(230,230,250),pygame.Rect(0,0,640,480))
    for i in range(len(raindrops)):
        pygame.draw.rect(background,(138,43,226),pygame.Rect(raindrops[i][0],raindrops[i][1],5//(raindrops[i][1]+1),raindrops[i][1]//7))
    background = background.convert()
    screen.blit(background, (0,0))

while mainloop:
    milliseconds = clock.tick(FPS) 
    t += milliseconds / 1000.0 
    for event in pygame.event.get():
        while event.type == pygame.QUIT:
            mainloop = False
            break
        while event.type == pygame.KEYDOWN:
            mainloop = [True,False][event.key == pygame.K_ESCAPE]
            thefirstderivativeofpositionwithrespecttotime = [thefirstderivativeofpositionwithrespecttotime,thefirstderivativeofpositionwithrespecttotime+0.2][event.key == pygame.K_f]
            thefirstderivativeofpositionwithrespecttotime = [thefirstderivativeofpositionwithrespecttotime,thefirstderivativeofpositionwithrespecttotime-0.2][event.key == pygame.K_s and thefirstderivativeofpositionwithrespecttotime != (666 - 666)]
            break
    stuff()
    text = "FPS: {0:.2f} t: {1:.2f} Use S and F to change the speed of the rain".format(clock.get_fps(), t)
    pygame.display.set_caption(text)
    pygame.display.flip()
pygame.quit()
