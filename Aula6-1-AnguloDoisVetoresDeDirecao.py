from locale import normalize
import pygame, sys
import numpy as np
from pygame.locals import *
###############################
#PRODUTO INTERNO - DOT FUNCTION
#CALCULAR ANGULO
############################### 
pygame.init()
screen = pygame.display.set_mode((400,300))

fpsClock=pygame.time.Clock()
FPS = 15 #num segundos 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255,0,0)

v_pos_blue=[0,100]
v_direcao_blue=[3,0]

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
    v_normalized = v_direcao_blue/np.linalg.norm(v_direcao_blue)
    v_velocity=np.multiply(speed, v_normalized)
    v_pos_blue=np.add(v_pos_blue,v_velocity)     
    pygame.draw.circle( screen, WHITE, v_pos_blue, 4)
    
    v_normalized2 = v_direcao_red/np.linalg.norm(v_direcao_red)
    v_pos_red=np.add(v_pos_red,v_direcao_red)
    pygame.draw.circle( screen, RED, v_pos_red, 4)

#Angle between two vectors using dot product is, θ = arccos [ (a · b) / (|a| |b|) ]
    produto_interno=np.dot(v_direcao_blue, v_direcao_red)
    magnitude_blue=np.linalg.norm(v_direcao_blue)
    magnitude_red=np.linalg.norm(v_direcao_red)
    produto_magnitudes=np.multiply(magnitude_blue,magnitude_red)
    angulo = np.arccos(np.divide(produto_interno,produto_magnitudes))
    

#    To convert any given angle from the measure of degrees to radians, 
#    the value has to be multiplied by π/180. Where the value of π = 22/7 or 3.14 
    print(np.radians(angulo))
   # print(angulo*3.14/180)
#    Pi radians are equal to 180 degree
    print(np.degrees(angulo))
    #print(angulo*180/np.pi)
    print("---")
    pygame.display.update()

    fpsClock.tick(FPS)
    


