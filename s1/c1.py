import random
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640,480))
clock = pygame.time.Clock()

mainloop = True
FPS = 30
t = 0.0

starcount = 20
stars = [[random.randint(0,640),random.randint(0,480)] for i in range(starcount)]
def stuff():
    background = pygame.Surface(screen.get_size())
    for i in range(starcount):
        pygame.draw.circle(background,(255,255,255),(stars[i][0],stars[i][1]),2)
        background = background.convert()
        screen.blit(background, (0,0))
    for i in range(starcount):
        stars[i][0] = [random.randint(0,640),int(stars[i][0] + (stars[i][0] - 320)/4)][stars[i][0]<640 and stars[i][0]>0]
        stars[i][1] = [random.randint(0,480),int(stars[i][1] + (stars[i][1] - 240)/4)][stars[i][1]<640 and stars[i][1]>0]
        while stars[i] == [320,240]:
            stars[i] = [random.randint(0,640),random.randint(0,480)]

while mainloop:
    milliseconds = clock.tick(FPS) 
    t += milliseconds / 1000.0 
    for event in pygame.event.get():
        while event.type == pygame.QUIT:
            mainloop = False
            break
        while event.type == pygame.KEYDOWN:
            mainloop = [True,False][event.key == pygame.K_ESCAPE]
            break
    
    stuff()
    
    text = "FPS: {0:.2f} t: {1:.2f}".format(clock.get_fps(), t)
    pygame.display.set_caption(text)
    pygame.display.flip()
pygame.quit()

print("That was",t,"seconds.")
