import pygame, sys
import numpy as np

from pygame.locals import *


pygame.init()
pygame.display.set_caption("Grafico") 
DISPLAYSURF = pygame.display.set_mode((400,300))
WHITE = (255, 255, 255)

p0 = [200, 150]
p1 = [150, 200]
p2 = [250, 200]

pygame.draw.line(DISPLAYSURF, WHITE, p0, p1, 1)
pygame.draw.line(DISPLAYSURF, WHITE, p1, p2, 1)
pygame.draw.line(DISPLAYSURF, WHITE, p2, p0, 1)

while True: #Main loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()

