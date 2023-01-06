import pygame, sys
import numpy as np

from pygame.locals import *

pygame.init()
pygame.display.set_caption("Aula 8 3") 
DISPLAYSURF = pygame.display.set_mode((400,300))
WHITE = (255, 255, 255)

angulo=10
theta = np.radians(angulo)
#Matriz de rotação
R = np.matrix([[np.cos(theta), -1*np.sin(theta)], 
               [np.sin(theta), np.cos(theta)]])

p0 = [200, 150]
p1 = [150, 200]
p2 = [250, 200]
while True: #Main loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.draw.line(DISPLAYSURF, WHITE, p0, p1, 1)
    pygame.draw.line(DISPLAYSURF, WHITE, p1, p2, 1)
    pygame.draw.line(DISPLAYSURF, WHITE, p2, p0, 1)
    
    p0_linha=np.matmul(R,p0)
    p0= [p0_linha[0,0], p0_linha[0,1]]
    p1_linha=np.matmul(R,p1)
    p1= [p1_linha[0,0], p1_linha[0,1]]
    p2_linha=np.matmul(R,p2) 
    p2= [p2_linha[0,0], p2_linha[0,1]]

    pygame.display.update()

