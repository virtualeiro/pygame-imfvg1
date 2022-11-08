import pygame, sys
from pygame.locals import *
import math
import numpy

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400,300))

fpsClock=pygame.time.Clock()
FPS = 30 #num segundos 
x1=10
y1=250
x2=x1+1 
y2=y1+1
a=0
image = pygame.image.load('boat.png')
image = pygame. transform. scale(image, (30, 28))
DISPLAYSURF.blit(image, (0, 0))
back = pygame.image.load('back.JPG')

while True: #Main loop--

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # copying the image surface object
    # to the display surface object at
    # (0, 0) coordinate.    
    x1=x1+1
    a=a+numpy.pi/20 

    DISPLAYSURF.blit(back, (40, 0))
    
    amplitude=10
    #pygame.draw.circle( DISPLAYSURF, (255,0,0), [x1, y1+amplitude*math.cos(a)], 1) 
    DISPLAYSURF.blit(image, (x1, y1+amplitude*math.cos(a)))
    
    pygame.display.update()
    
    #pygame.time.wait(10)
    fpsClock.tick(FPS)
    
    DISPLAYSURF.fill((0,0,0))
    #pygame.display.flip()
    


