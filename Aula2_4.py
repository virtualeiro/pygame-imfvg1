import pygame, sys
import numpy as np
from pygame.locals import *
###############################
#VETORES
#NORMALIZACAO
#DIRECAO E MOVIMENTO
###############################
pygame.init()
screen = pygame.display.set_mode((400,300))

fpsClock=pygame.time.Clock()
FPS = 15 #num segundos 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

v_pos=[0,100]
v_direcao=[1,0]
while True: #Main loop--
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
                         
    screen.fill(BLACK)
    #1- SO DIRECAO LINEAR
    v_pos=np.add(v_pos,v_direcao)
    
    
    #4-COM VENTO for�a oposta
    forca=-0.75
    v_direcao_oposta=np.multiply(forca,v_direcao)
    v_pos=np.add(v_pos, v_direcao_oposta)
    
    pygame.draw.circle( screen, WHITE, v_pos, 4)
        
    pygame.display.update()

    fpsClock.tick(FPS)
    