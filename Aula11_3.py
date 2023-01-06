# -*- coding: latin-1 -*-
import pygame, sys
import numpy as np

from pygame.locals import *

pygame.init()
fpsClock=pygame.time.Clock()


FPS = 3 #num segundos 
pygame.display.set_caption("11_3-Escala") 
DISPLAYSURF = pygame.display.set_mode((800,600))
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
VERTICE=50
#1
p0 = [DISPLAYSURF.get_width()/2, DISPLAYSURF.get_height()/2-VERTICE/2]
p1 = [DISPLAYSURF.get_width()/2-VERTICE, DISPLAYSURF.get_height()/2+VERTICE]
p2 = [DISPLAYSURF.get_width()/2+VERTICE, DISPLAYSURF.get_height()/2+VERTICE]

#--Função desenha_triangulo----------------------------------
def desenha_triangulo(ponto0, ponto1, ponto2, cor):
   pygame.draw.line(DISPLAYSURF, cor, ponto0, ponto1, 1)
   pygame.draw.line(DISPLAYSURF, cor, ponto1, ponto2, 1)
   pygame.draw.line(DISPLAYSURF, cor, ponto2, ponto0, 1)
   return
#------------------------------------------------------------

#--Função Rotação______--------------------------------------
def rotacao(ponto, angulo):
#significa encontrar uma circunfrencia centrada na origem que passa pela coordenada
#x'=x.cos@ - y.sin@
#y'=y.sin@ + y.cos@
#Anti-horario  
   ###Forma linar
   #ponto_retorno=(0,0)
   #ponto_retorno=(ponto[0]*np.cos(angulo) - ponto[1]*np.sin(angulo), 
   #               ponto[0]*np.sin(angulo) + ponto[1]*np.cos(angulo)) 
   #return ponto_retorno

   ####Forma matricial
   mRot=np.array([[np.cos(angulo), -np.sin(angulo)],[np.sin(angulo), np.cos(angulo)]])
   res=np.dot(mRot, [ponto[0], ponto[1]])
   return (res[0], res[1])

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
pr0=rotacao(p0,np.pi/10)#np.radians(angulo)
pr1=rotacao(p1,np.pi/10)
pr2=rotacao(p2,np.pi/10)
desenha_triangulo(pr0,pr1,pr2,RED)
0


#3
#Rotação com tranladação para origem 1/3
#Deslocamento para origem
ponto_central = ((p0[0]+p1[0]+p2[0])/3, (p0[1]+p1[1]+p2[1])/3)
pt0=translacao(p0,-1*ponto_central[0],-1*ponto_central[1])
pt1=translacao(p1,-1*ponto_central[0],-1*ponto_central[1])
pt2=translacao(p2,-1*ponto_central[0],-1*ponto_central[1])
desenha_triangulo(pt0,pt1,pt2, BLUE)

#4 Rotaçao com tranladação para origem 2/3
pr0=rotacao(pt0,np.pi/10)#np.radians(angulo)
pr1=rotacao(pt1,np.pi/10)
pr2=rotacao(pt2,np.pi/10)
desenha_triangulo(pr0,pr1,pr2,BLUE)

#5 Rotação com tranladação para origem 3/3
#Devolução (deslocamento) ao ponto inicial
p0_rodado=translacao(pr0, ponto_central[0], ponto_central[1])
p1_rodado=translacao(pr1, ponto_central[0], ponto_central[1])
p2_rodado=translacao(pr2, ponto_central[0], ponto_central[1])
desenha_triangulo(p0_rodado, p1_rodado, p2_rodado, GREEN)

pygame.display.update()

while True: #Main loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()










