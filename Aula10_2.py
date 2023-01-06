# -*- coding: latin-1 -*-
import pygame, sys
import numpy as np

from pygame.locals import *

pygame.init()
fpsClock=pygame.time.Clock()


FPS = 3 #num segundos 
pygame.display.set_caption("10_2-Translation") 
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

#--Função translação-----------------------------------------
def translacao(ponto, dx, dy):
#x'=x+dx 
#y'=y+dy
   ###Forma linear 
   #ponto_retorno=(0,0)
   #ponto_retorno=(ponto[0]+dx, ponto[1]+dy)
   #return ponto_retorno
   ###Forma matricial 
   mTrans=[dx,dy]
   res=np.add(mTrans,ponto)
   return (res[0], res[1])
#------------------------------------------------------------

desenha_triangulo(p0, p1, p2, WHITE) 
#1
#Desloca -50,-50
pt0=translacao(p0,-50,-50)
pt1=translacao(p1,-50,-50)
pt2=translacao(p2,-50,-50)
desenha_triangulo(pt0,pt1,pt2, RED)
#2
#Tranladação para origem
ponto_central = ((p0[0]+p1[0]+p2[0])/3, (p0[1]+p1[1]+p2[1])/3)
pt0=translacao(p0,-1*ponto_central[0],-1*ponto_central[1])
pt1=translacao(p1,-1*ponto_central[0],-1*ponto_central[1])
pt2=translacao(p2,-1*ponto_central[0],-1*ponto_central[1])
desenha_triangulo(pt0,pt1,pt2, GREEN)

pygame.display.update()
while True: #Main loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()







