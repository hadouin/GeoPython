# Geopython pygame
import pygame
from settings import *

pygame.init()

pygame.display.set_caption("Geopython")
window_surface = pygame.display.set_mode(window_resolution)

player = pygame.Rect(10, 10, 150, 65)
pygame.draw.rect(window_surface, white_color, player)
pygame.display.flip()


launched = True 
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False 
    # Corps du programme
    pygame.display.flip()