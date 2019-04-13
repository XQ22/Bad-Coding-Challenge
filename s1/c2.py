import math
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640,480))
clock = pygame.time.Clock()

mainloop = True
FPS = 30
t = 0.0

# Beginning point
nodes = [[0,0,0]]
faces = [[0,0,0,0]]

def translate(α,β,γ):
    for i in range(len(nodes)):
        ν = nodes[i]
        ν[0] = ν[0] + α
        ν[1] = ν[1] + β
        ν[2] = ν[2] + γ
        
def rotateX(θ): #3D shape code adapted from the KhanAcademy (https://www.khanacademy.org/computing/computer-programming/programming-games-visualizations#programming-3d-shapes).
    σ = math.sin(θ)
    κ = math.cos(θ)
    for i in range(len(nodes)):
        ν = nodes[i]
        ζ = ν[1]
        ξ = ν[2]
        ν[1] = ζ*κ - ξ*σ
        ν[2] = ζ*κ + ξ*σ
def rotateY(θ):
    σ = math.sin(θ)
    κ = math.cos(θ)
    for i in range(len(nodes)):
        ν = nodes[i]
        ζ = ν[0]
        ξ = ν[2]
        ν[0] = ζ*κ - ξ*σ
        ν[2] = ζ*κ + ξ*σ
def rotateZ(θ):
    σ = math.sin(θ)
    κ = math.cos(θ)
    for i in range(len(nodes)):
        ν = nodes[i]
        ζ = ν[0]
        ξ = ν[1]
        ν[0] = ζ*κ - ξ*σ
        ν[1] = ζ*κ + ξ*σ
def cube(α,β,γ,ω):
    κ = len(nodes)
    nodes.append([α,β,γ])
    nodes.append([α+ω,β,γ])
    nodes.append([α,β+ω,γ])
    nodes.append([α+ω,β+ω,γ])
    nodes.append([α,β,γ+ω])
    nodes.append([α+ω,β,γ+ω])
    nodes.append([α,β+ω,γ+ω])
    nodes.append([α+ω,β+ω,γ+ω])
    faces.append([κ+0,κ+1,κ+3,κ+2])
    faces.append([κ+4,κ+5,κ+7,κ+6])
    faces.append([κ+0,κ+1,κ+5,κ+4])
    faces.append([κ+2,κ+3,κ+7,κ+6])
    faces.append([κ+0,κ+2,κ+4,κ+6])
    faces.append([κ+1,κ+3,κ+7,κ+5])
def menger(г,α,β,γ):
    while г == 1:
        cube(α,β,γ,5)
        cube(α+5,β,γ,5)
        cube(α+10,β,γ,5)
        cube(α,β+5,γ,5)
        cube(α+10,β+5,γ,5)
        cube(α,β+10,γ,5)
        cube(α+5,β+10,γ,5)
        cube(α+10,β+10,γ,5)
        cube(α,β,γ+10,5)
        cube(α+5,β,γ+10,5)
        cube(α+10,β,γ+10,5)
        cube(α,β+5,γ+10,5)
        cube(α+10,β+5,γ+10,5)
        cube(α,β+10,γ+10,5)
        cube(α+5,β+10,γ+10,5)
        cube(α+10,β+10,γ+10,5)
        cube(α,β,γ+5,5)
        cube(α,β+10,γ+5,5)
        cube(α+10,β,γ+5,5)
        cube(α+10,β+10,γ+5,5)
        break
    while г > 1:
        ς = 5*(3**(г-1))
        menger(г-1,α,β,γ)
        menger(г-1,α+ς,β,γ)
        menger(г-1,α+ς+ς,β,γ)
        menger(г-1,α,β+ς,γ)
        menger(г-1,α+ς+ς,β+ς,γ)
        menger(г-1,α,β+ς+ς,γ)
        menger(г-1,α+ς,β+ς+ς,γ)
        menger(г-1,α+ς+ς,β+ς+ς,γ)
        menger(г-1,α,β,γ+ς+ς)
        menger(г-1,α+ς,β,γ+ς+ς)
        menger(г-1,α+ς+ς,β,γ+ς+ς)
        menger(г-1,α,β+ς,γ+ς+ς)
        menger(г-1,α+ς+ς,β+ς,γ+ς+ς)
        menger(г-1,α,β+ς+ς,γ+ς+ς)
        menger(г-1,α+ς,β+ς+ς,γ+ς+ς)
        menger(г-1,α+ς+ς,β+ς+ς,γ+ς+ς)
        menger(г-1,α,β,γ+ς)
        menger(г-1,α,β+ς+ς,γ+ς)
        menger(г-1,α+ς+ς,β,γ+ς)
        menger(г-1,α+ς+ς,β+ς+ς,γ+ς)
        break
menger(4,243.75,163.75,-76.25)
def stuff():
    background = pygame.Surface(screen.get_size())
    for i in range(len(faces)):
        ν = faces[i]
        ǽ = []
        for j in range(len(ν)):
            ə = ν[j]
            ǽ.append((nodes[ə][0],nodes[ə][1]))
        pygame.draw.polygon(background,(125,125,0),ǽ)
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
            #OOOOOOOOOOOOOOOOOooooh I'm a spooky ghost leaving comments to haunt your code.
            while event.key == pygame.K_s:
                translate(-320,-240,0)
                rotateX(-1)
                translate(320,240,0)
                break
            while event.key == pygame.K_f:
                translate(-320,-240,0)
                rotateX(1)
                translate(320,240,0)
                break
            while event.key == pygame.K_d:
                translate(-320,-240,0)
                rotateY(-1)
                translate(320,240,0)
                break
            while event.key == pygame.K_e:
                translate(-320,-240,0)
                rotateY(1)
                translate(320,240,0)
                break
            break
    stuff()
    text = "FPS: {0:.2f} t: {1:.2f} Use ESDF to rotate".format(clock.get_fps(), t)
    pygame.display.set_caption(text)
    pygame.display.flip()
pygame.quit()
