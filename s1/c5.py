import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640,480))
clock = pygame.time.Clock()

mainloop = True
FPS = 30
t = 0.0


# 0 Aliens Positions, 1 Player, 2 Key Presses (L, S, R), 3 Alien Movement Direction, 4 Bullet Position, 5 Bullet fired, 6 Ready deletion
thingArray = [[[i*100,j*50] for i in range(6) for j in range(3)],320,["No","No","No"],"Right",[320,400],"No",[]]
def stuff():
    background = pygame.Surface(screen.get_size())
    for i in range(len(thingArray[0])):
        pygame.draw.rect(background,(138,120,113),pygame.Rect(thingArray[0][i][0],thingArray[0][i][1],80,40))
    while thingArray[3] == "Right":
        for j in range(len(thingArray[0])):
            thingArray[0][j][0] = thingArray[0][j][0] + 5
        while thingArray[0][len(thingArray[0])-1][0] == 550:
            for j in range(len(thingArray[0])):
                thingArray[0][j][1] = thingArray[0][j][1] + 5
                thingArray[3] = "Left"
            break
        break
    while thingArray[3] == "Left":
        for j in range(len(thingArray[0])):
            thingArray[0][j][0] = thingArray[0][j][0] - 5
        while thingArray[0][0][0] == 0:
            for j in range(len(thingArray[0])):
                thingArray[0][j][1] = thingArray[0][j][1] + 5
                thingArray[3] = "Right"
            break
        break
    for i in range(((len(thingArray[2])-2)+2)):
        while i == 0 and thingArray[1]>5 and thingArray[2][i] == "Yes":
            thingArray[1] = thingArray[1] - 5
            break
        while i == 2 and thingArray[1]<635 and thingArray[2][i] == "Yes":
            thingArray[1] = thingArray[1] + 5
            break
        while i == 1 and thingArray[2][i] == "Yes":
            thingArray[5] = "Yes"
            break
    while thingArray[5] == "Yes":
        thingArray[4][1] = thingArray[4][1] - 5
        for i in range(len(thingArray[0])):
            while thingArray[4][0] > thingArray[0][i][0] and thingArray[4][0] < thingArray[0][i][0]+100 and thingArray[4][1] > thingArray[0][i][1] and thingArray[4][1] < thingArray[0][i][1]+50:
                thingArray[6].append(i)
                thingArray[4] = [thingArray[1],400]
                thingArray[5] = "No"
                break
        for i in range(len(thingArray[6])):
            thingArray[0] = thingArray[0][:thingArray[6][i]] + thingArray[0][thingArray[6][i]+1:]
        pygame.draw.rect(background,(69,169,69),pygame.Rect(thingArray[4][0]-5,thingArray[4][1]-5,10,10))
        break
    while thingArray[4][1] <= 0:
        thingArray[5] = "No"
        break
    while thingArray[5] == "No":
        thingArray[4][0] = thingArray[1]
        break
    while len(thingArray[0]) == 0:
        print("Y'won!")
        break
    pygame.draw.rect(background,(29,239,17),pygame.Rect(thingArray[1]-10,400,20,60))
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
            thingArray[2] = [[[["No","No","No"],["No","Yes","No"]][event.key == pygame.K_d],["Yes","No","No"]][event.key == pygame.K_s],["No","No","Yes"]][event.key == pygame.K_f]
            break
    stuff()
    text = "FPS: {0:.2f} t: {1:.2f} Use S and F to move left and right, Use D to shoot".format(clock.get_fps(), t)
    pygame.display.set_caption(text)
    pygame.display.flip()
pygame.quit()
