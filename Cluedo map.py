import pygame, sys
from pygame.locals import QUIT

WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cluedo")
WHITE = (255, 255, 255)
cluedoMap = pygame.image.load('Cluedo map.png').convert_alpha()
cluedoBoard = pygame.transform.scale(cluedoMap, (600, 600))
mouse = pygame.mouse.get_pos()

run = True
while run:

  WIN.fill((202,228,241))
  WIN.blit(cluedoMap, (0,0))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
  pygame.display.update()


pygame.quit()
