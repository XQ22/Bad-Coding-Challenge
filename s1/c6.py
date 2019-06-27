import pygame
import random
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640,480))
clock = pygame.time.Clock()

mainloop = True
FPS = 30
t = 0.0


cells = [[random.randint(0,640),random.randint(0,480),20,random.randint(-10,10),random.randint(-10,10)] for i in range(2)]

def split(*n):
    cells.append([cells[n[0]][0]+cells[n[0]][3],cells[n[0]][1]+cells[n[0]][4],int(float(cells[n[0]][2])/(2**(2**-1))),cells[n[0]][3],cells[n[0]][4]])
    cells.append([cells[n[0]][0]-cells[n[0]][3],cells[n[0]][1]+cells[n[0]][4],int(float(cells[n[0]][2])/(2**(2**-1))),cells[n[0]][3],cells[n[0]][4]])
    del cells[n[0]]
def A(*n):
    return sum(n)
    
def stuff():
    background = pygame.Surface(screen.get_size())
    for i in range(len(cells)):
        pygame.draw.circle(background,(143,53,249),(cells[i][0],cells[i][1]),cells[i][2])
        cells[i][0] = A(cells[i][0],cells[i][3])
        cells[i][1] = A(cells[i][1],cells[i][4])
        cells[i][3] = random.randint(-10,10)
        cells[i][4] = random.randint(-10,10)
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
            for i in range(len(cells)):
                split(i)
            break
    stuff()
    text = "FPS: {0:.2f} t: {1:.2f} Press any key to split all the cells".format(clock.get_fps(), t)
    pygame.display.set_caption(text)
    pygame.display.flip()
pygame.quit()
