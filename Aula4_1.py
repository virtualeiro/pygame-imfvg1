import pygame, sys
from pygame.locals import *
import math
pygame.init()
DISPLAYSURF = pygame.display.set_mode((400,300))
COR_FUNDO=(255,255,255)
ang=0
while True: #Main loop--
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
     
    ang=ang+0.01 
    val=(math.cos(ang)*255+255)/2
    val=(math.cos(ang)+1)/2*255
    print(val)
    COR_FUNDO=(val,255,255)     
    DISPLAYSURF.fill(COR_FUNDO)
    pygame.display.update()

  
    
