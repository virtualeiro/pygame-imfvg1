import pygame, sys
from pygame.locals import *
import math
pygame.init()
DISPLAYSURF = pygame.display.set_mode((400,300))
WHITE=(255,255,255)
ang=0
posicao_x=0
while True: #Main loop--
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    DISPLAYSURF.fill((0,0,0))
    ang=ang+0.1 
    raio=10
    #1 SO CIRCULO AO CENTRO 
    #x = 200 + math.sin(ang)*raio
    #y = 200 + math.cos(ang)*raio

    #2 A RODAR DA ESQUERDA PARA A DIREITA
    x = math.sin(ang)*raio
    y = math.cos(ang)*raio
   
    posicao_x=posicao_x+0.01
    x=x+posicao_x
    y=y+200
    pygame.draw.circle( DISPLAYSURF, WHITE, [x,y], 1)

    pygame.display.update()

  
    
