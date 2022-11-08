import pygame, sys
from pygame.locals import *
import math
import numpy as np
pygame.init()
DISPLAYSURF = pygame.display.set_mode((400,300))
WHITE=(255,255,255)
ang=np.pi
posicao=0

while True: #Main loop--
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
               ang=ang+np.pi/10
            if event.key == pygame.K_LEFT:
               ang=ang-np.pi/10 
    DISPLAYSURF.fill((0,0,0))
    inicio_linha=(200,300)

    #end_line=CENTRO_LINHA+v_linha
    #print(end_line)
    raio=100
    x = math.sin(ang)*raio
    y = math.cos(ang)*raio
    fim_linha=np.add(inicio_linha, [x,y])
    pygame.draw.circle( DISPLAYSURF, WHITE, [200,300], 100,1)
    pygame.draw.line(DISPLAYSURF, WHITE, inicio_linha, fim_linha, 2)
    pygame.display.update()

  
    
