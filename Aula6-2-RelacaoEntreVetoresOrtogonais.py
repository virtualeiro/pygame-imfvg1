from locale import normalize
import pygame, sys
import numpy as np
from pygame.locals import *
###############################
#PRODUTO INTERNO - DOT FUNCTION
#CALCULAR RELACAO ENTRE VETORES DE DIRECAO
# α • b = |a| |b| cos θ
#O produto escalar calcula uma quantidade escalar. 
#Esta quantidade é geralmente distância ou comprimento.
#O produto escalar, comumente usado na geometria euclidiana, 
#é um caso especial dentro do chamado produto interno.
#O produto interno entre dois vetores é um número real que relaciona o módulo desses vetores, 
#isto é, seu comprimento, e o ângulo entre eles. 
#Para calculá-lo, é necessário, portanto, conhecer seus comprimentos 
#e o ângulo que eles formam.
###############################
pygame.init()
screen = pygame.display.set_mode((400,300))

fpsClock=pygame.time.Clock()
FPS = 15 #num segundos 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255,0,0)

v_pos_1=[0,100]
v_direcao_1=[3,0]

v_pos_red=[100,100]
v_direcao_red=[0,1]
#v_direcao_red=[1,1]
#v_direcao_red=[1,0]

while True: #Main loop--
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(BLACK)
    
    speed=4
    v_normalized = v_direcao_1/np.linalg.norm(v_direcao_1)
    v_velocity=np.multiply(speed, v_normalized)
    v_pos_1=np.add(v_pos_1,v_velocity)     
    pygame.draw.circle( screen, WHITE, v_pos_1, 4)
    
    v_pos_red=np.add(v_pos_red,v_direcao_red)
    v_normalized2 = v_direcao_red/np.linalg.norm(v_direcao_red)
    pygame.draw.circle( screen, RED, v_pos_red, 4)
  
#Atencao fazer operacao com vetores normalizados
#if the dot product is equal to 1, 
#it means that both vectors have the same direction. 
    if(np.dot(v_normalized2, v_normalized)==1):
           print("Same direction")
#If the dot product is 0, 
#it means that both vectors are perpendicular on each other. 
    elif(np.dot(v_normalized2, v_normalized)==0): 
           print("Perpendicular")
#Finally, if the dot product is -1, 
#it means that both vectors are heading in opposite directions.
    elif(np.dot(v_normalized2, v_normalized)==-1): 
           print("Opposite directions")    
    #pygame.draw.circle( screen, RED, pygame.mouse.get_pos(), 1)
    else :print("Non orthogonal")
        
    font = pygame.font.SysFont('Arial', 25)

    #angulo=10
    screen.blit(font.render("Valor do angulo", True, WHITE),(10, 20))

    pygame.display.update()

    fpsClock.tick(FPS)
    

