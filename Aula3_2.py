import pygame, sys
from pygame.locals import *
import math
import numpy

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400,300))
ang=0
WHITE = (255,255,255)
while True: #Main loop--
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    ang=ang+0.1 
    #1 BLINKING SCREEN
    #val=(math.cos(a)*255+255)/2
    
    #DISPLAYSURF.fill((val,0,0))
    #dimensions = pygame.display.get_window_size()
    #pygame.draw.circle( DISPLAYSURF, WHITE, [dimensions[0]/2, dimensions[1]/2], 40)
    #2 CIRCLE 
    raio=100
    x = 200 + math.sin(ang)*raio ;
    y = 200 + math.cos(ang)*raio;

    pygame.draw.circle( DISPLAYSURF, WHITE, [x,y], 1)

    
    pygame.display.update()
