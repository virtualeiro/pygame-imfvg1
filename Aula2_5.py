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
           # print(event.key)
           # print(chr(event.key))
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    #5-COM TECLAS
            if event.key == pygame.K_RIGHT:
                v_direcao=[1,0]
            if event.key == pygame.K_LEFT:
                v_direcao=[-1,0]
            if event.key == pygame.K_UP:
                v_direcao=[0,-1]
            if event.key == pygame.K_DOWN:
                v_direcao=[0,1]    
                         
    screen.fill(BLACK)
    #1- SO DIRECAO LINEAR
    v_pos=np.add(v_pos,v_direcao)
    #2- COM SPEED 
    speed=4
    # norm = magnitude 
    #Vector unitario
    v_normalized = v_direcao/np.linalg.norm(v_direcao)
    v_velocity=np.multiply(speed, v_normalized)
    v_pos=np.add(v_pos,v_velocity) 
    
    #3-COM GRAVIDADE
    v_forca_gravitacional=[0,0.5]
    v_pos=np.add(v_pos, v_forca_gravitacional)
    
    #4-COM VENTO 
    forca=-0.75
    v_direcao_oposta=np.multiply(forca,v_direcao)
    v_pos=np.add(v_pos, v_direcao_oposta)
    
    pygame.draw.circle( screen, WHITE, v_pos, 4)
        
    pygame.display.update()

    fpsClock.tick(FPS)
    