# -*- coding: latin-1 -*-
import pygame, sys
import numpy as np
from pygame.locals import *

pygame.init()
pygame.display.set_caption("10_1-Triangulo") 
DISPLAYSURF = pygame.display.set_mode((800,600))
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ARESTA=50
centroX=DISPLAYSURF.get_width()/2
centroY=DISPLAYSURF.get_height()/2
#1
p0 = [centroX, centroY - ARESTA/2]
p1 = [centroX-ARESTA, centroY + ARESTA ]
p2 = [centroX+ARESTA, centroY + ARESTA ]

#--Função desenha_triangulo---------------------------------
def desenha_triangulo(ponto0, ponto1, ponto2, cor):
   pygame.draw.line(DISPLAYSURF, cor, ponto0, ponto1, 1)
   pygame.draw.line(DISPLAYSURF, cor, ponto1, ponto2, 1)
   pygame.draw.line(DISPLAYSURF, cor, ponto2, ponto0, 1)
   return
#------------------------------------------------------------

desenha_triangulo(p0, p1, p2, WHITE) 
pygame.display.update()

while True: #Main loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()




