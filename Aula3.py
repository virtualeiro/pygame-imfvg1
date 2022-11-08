import pygame, sys
from pygame.locals import *
import math
import numpy

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400,300))


x1=10
y1=50
a=0
WHITE = (255, 255, 255)

y2=y1+50 
y3=y1+100 
y4=y1+150
y5=y1+200


while True: #Main loop--
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    x1=x1+1
    a=a+0.1 

    pygame.draw.circle( DISPLAYSURF, WHITE, [x1, y1 + math.cos(a)], 1)

    amplitude=10
    pygame.draw.circle( DISPLAYSURF, (255,0,0), [x1, y2 + amplitude*math.cos(a)], 1) 
    
    fase=numpy.pi
    pygame.draw.circle( DISPLAYSURF, (255,126,126), [x1, y3 + amplitude * math.cos(a + fase)], 1) 
    
    frequencia=0.5
    pygame.draw.circle( DISPLAYSURF, (0,0,255), [x1, y4 + amplitude*math.cos(a * frequencia)], 1) 
    pygame.draw.circle( DISPLAYSURF, (0,255,0), [x1, y5 + amplitude*math.cos(2*frequencia*a)], 1) 
    pygame.draw.circle( DISPLAYSURF, (255,255,0), [x1, y5 + amplitude*math.cos(4*frequencia*a)], 1) 
    
    pygame.display.update()

    #fpsClock.tick(FPS)
    