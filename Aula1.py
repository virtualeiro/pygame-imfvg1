# -*- coding: cp860 -*-

import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400,300))
frase= "Hello World!"

pygame.display.set_caption(frase) 

#EXERCICIO 2 FAZ LINHA
#WHITE = (255, 255, 255)
#RED   = (255, 0, 0)
#DISPLAYSURF.fill(WHITE)
#pygame.draw.line(DISPLAYSURF, RED, (60, 60), (120, 60), 4)

while True: #Main loop
    #CLOSE WINDOW
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
#            if event.key == pygame.K_RIGHT:
#                location += 1
    pygame.display.update()


