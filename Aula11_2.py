import pygame, sys
import numpy as np
from pygame.locals import *

pygame.init()
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

#--Função desenha_triangulo----------------------------------
def desenha_triangulo(ponto0, ponto1, ponto2, cor):
   pygame.draw.line(DISPLAYSURF, cor, ponto0, ponto1, 1)
   pygame.draw.line(DISPLAYSURF, cor, ponto1, ponto2, 1)
   pygame.draw.line(DISPLAYSURF, cor, ponto2, ponto0, 1)
   return
#------------------------------------------------------------

#--Função escalonamento--------------------------------------
def escala(ponto, value):
    #y'=sy.y 
    #x'=sx.x
    ponto_retorno=(0,0)
    ponto_retorno=(value*ponto[0], value*ponto[1])
    return ponto_retorno
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

#1
desenha_triangulo(p0, p1, p2, WHITE) 
#2
ps0= escala(p0,1.5)
ps1= escala(p1,1.5)
ps2= escala(p2,1.5)
desenha_triangulo(ps0,ps1,ps2, RED)

#3
#Esclonamento com tranladação para origem 1/3
#Deslocamento para origem
ponto_central = ((p0[0]+p1[0]+p2[0])/3, (p0[1]+p1[1]+p2[1])/3)
pt0=translacao(p0,-1*ponto_central[0],-1*ponto_central[1])
pt1=translacao(p1,-1*ponto_central[0],-1*ponto_central[1])
pt2=translacao(p2,-1*ponto_central[0],-1*ponto_central[1])
desenha_triangulo(pt0,pt1,pt2, BLUE)

#4 Escalonamento com tranladação para origem 2/3
#Escalonamento
pt0_1=escala(pt0,1.5)
pt1_1=escala(pt1,1.5)
pt2_1=escala(pt2,1.5)

#5 Escalonamento com tranladação para origem 3/3
#Devolução (deslocamento) ao ponto inicial
p0_escalado=translacao(pt0_1, ponto_central[0], ponto_central[1])
p1_escalado=translacao(pt1_1, ponto_central[0], ponto_central[1])
p2_escalado=translacao(pt2_1, ponto_central[0], ponto_central[1])
desenha_triangulo(p0_escalado, p1_escalado, p2_escalado, GREEN)

pygame.display.update()

while True: #Main loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()








