# -*- coding: cp860 -*-

import pygame, sys
from pygame.locals import *
import numpy as np

BLUE = (0,0,255)
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)

pygame.init()
screen = pygame.display.set_mode((400,300))
frase= "MOVING"
font = pygame.font.SysFont('Arial', 20)
pygame.display.set_caption(frase)

cnt_x=screen.get_width()/2
cnt_y=screen.get_height()/2
max_x=screen.get_width()
max_y=screen.get_height()

pos_circle =[cnt_x, cnt_y]
image = pygame.image.load('arrow.png').convert_alpha()
image = pygame. transform. scale(image, (30, 28))

while True: #Main loop
    #parte fixa 
    screen.fill((WHITE))
    pygame.draw.line(screen, RED,(0,cnt_y), (max_x,cnt_y), 1)
    pygame.draw.line(screen, RED,(cnt_x,0), (cnt_x,max_y), 1)
    
    #
    pygame.draw.circle(screen, BLUE, pos_circle, 10)
    pos_circle=np.round(pos_circle,2)    
    screen.blit(font.render("seta movel" + str(pos_circle), True, BLACK), (0,10))

    pygame.draw.line(screen, (0,255,0),(cnt_x,cnt_y), pos_circle,1)
    
    #Calcula o angulo
    #arctan2
    #The single-argument arctangent function cannot distinguish between diametrically opposite directions
    #https://en.wikipedia.org/wiki/Atan2
    angulo = np.arctan2( cnt_y - pos_circle[1], cnt_x - pos_circle[0])
    angulo_em_graus=np.degrees(angulo)
    angulo_em_graus=np.round(angulo_em_graus)
    screen.blit(font.render("[" + str(angulo_em_graus)+" graus]", True, BLACK), (pos_circle[0],pos_circle[1]+20))
    
    #Roda primeira seta
    rotimage = pygame.transform.rotate(image,-angulo_em_graus)
    rect = rotimage.get_rect(center=pos_circle)
    screen.blit(rotimage,rect) #Roda

    #Roda segunda seta (180 - o angulo que foi determinado), pois se uma olha numa direção a outra olha na direção oposta (senão teriamos que calcular de novo mudando a ordem dos factores (quem é o target, e quem é a origem))
    rotimage2 = pygame.transform.rotate(image,180-angulo_em_graus)
    rect = rotimage2.get_rect(center=(screen.get_width()/2,screen.get_height()/2))
    screen.blit(rotimage2,rect) #Roda
    screen.blit(font.render("[" +str(angulo_em_graus)+"] ["  + str(180-angulo_em_graus)+ "]", True, BLACK), (screen.get_width()/2,screen.get_height()/2))  
    
    #Processa teclado 
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
        
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        

    #CLOSE WINDOW
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    
    pygame.display.update()









