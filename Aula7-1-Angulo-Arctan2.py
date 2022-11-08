# -*- coding: cp860 -*-

import pygame, sys
from pygame.locals import *
import numpy as np
BLUE = (0,0,255)
WHITE=(255,255,255)
BLACK=(0,0,0)
RED = (255,0,0)
pygame.init()
screen = pygame.display.set_mode((400,300))
frase= "MOVING"
font = pygame.font.SysFont('Arial', 25)
pygame.display.set_caption(frase)

cnt_y=screen.get_height()/2
cnt_x=screen.get_width()/2
max_x=screen.get_width()
max_y=screen.get_height()

pos_circle =[cnt_x, cnt_y]

while True: #Main loop
    screen.fill((WHITE))

    pygame.draw.circle(screen, BLUE, pos_circle, 10)
    pos_circle=np.round(pos_circle,2)    
    screen.blit(font.render(str(pos_circle), True, BLACK), pos_circle)

    pygame.draw.line(screen, RED,(0,cnt_y), (max_x,cnt_y),1)
    pygame.draw.line(screen, RED,(cnt_x,0), (cnt_x,max_y),1)
   
    #https://www.cuemath.com/geometry/angle-between-vectors/
    #angulo=angle_between(pos_circle,(screen.get_width()/2, screen.get_height()/2))
    #angulo = math.atan2(enemy.y - self.y, enemy.x - self.x)
    pygame.draw.line(screen, (0,255,0),(cnt_x,cnt_y), pos_circle,1)
    #dot product = produto escalar
    #cross product = produto vectorial
    #Arctan retorna o ângulo, expresso em radianos, da tangente número.
    #A função ATAN2 devolve o ângulo entre o eixo x e um segmento de linha da origem (0;0) e o par de coordenadas especificado ("x";"y"), em radianos.
    #converte as coordenadas cartesianas (x,y) em polares (r,theta)
    #A função atan2 (y, x) pode ser usada em vez da função matemática arctan (y/x) devido ao seu domínio e imagem.
    angulo = np.arctan2( cnt_y - pos_circle[1],  cnt_x - pos_circle[0])

    angulo_em_graus=np.degrees(angulo)
    angulo_em_graus=np.round(angulo_em_graus)
    screen.blit(font.render(str(angulo_em_graus), True, BLACK), (cnt_x,cnt_y))

    """
        #The keyboard events (see pygame.event module) occur only once 
        #when the state of a key changes. 
        #The KEYDOWN event occurs once every time a key is pressed. 
        #KEYUP occurs once every time a key is released. 
        #Use the keyboard events for a single action or movement:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pos[0]-=1
                if event.key == pygame.K_RIGHT:
                    pos[0]+=1
                if event.key == pygame.K_UP:
                    pos[1]-=1
                if event.key == pygame.K_DOWN:
                    pos[1]+=1
    """
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pos_circle[0]-=0.1
        print(pos_circle)
    if keys[pygame.K_RIGHT]:
        pos_circle[0]+=0.1
        print(pos_circle)
    if keys[pygame.K_UP]:
        pos_circle[1]-=0.1
        print(pos_circle)
    if keys[pygame.K_DOWN]:
        pos_circle[1]+=0.1
        print(pos_circle)
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        

    #CLOSE WINDOW
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    
    pygame.display.update()







