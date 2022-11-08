import pygame, sys
from pygame.locals import *
import math
import numpy as np
pygame.init()
DISPLAYSURF = pygame.display.set_mode((400,300))
WHITE=(255,255,255)
ang=np.pi
posicao=0
speed =0
v_calibrador=(0,-1)
p_inicio_calibrador=(290,300)

while True: #Main loop--
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
               speed=speed+1               
            if event.key == pygame.K_DOWN:
               speed=speed-1

    DISPLAYSURF.fill((0,0,0))

    novo_v_calibrador=np.multiply(v_calibrador,speed*10)
    fim_calibrador=np.add(p_inicio_calibrador,novo_v_calibrador)
    
    pygame.draw.line(DISPLAYSURF, WHITE, p_inicio_calibrador, fim_calibrador, 10)
    pygame.display.update()

  
    
