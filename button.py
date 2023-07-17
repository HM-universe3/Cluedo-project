import pygame, sys
from pygame.locals import QUIT

WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cluedo")
WHITE = (255, 255, 255)
cluedoMap = pygame.image.load('Cluedo map.png').convert_alpha()
cluedoBoard = pygame.transform.scale(cluedoMap, (600, 600))
mouse = pygame.mouse.get_pos()


#load button images
garage_img = pygame.image.load("garage_button.png").convert_alpha()

class Button:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), (int(height * scale))))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.click = False


    def draw(self):
      action = False
       #get mouse position
      pos = pygame.mouse.get_pos()

       #check mouseover and clicked conditions
      if self.rect.collidepoint(pos):
        if pygame.mouse.get_pressed()[0] == 1 and self.click == False:
          self.click = True
          action = True
      if pygame.mouse.get_pressed()[0] == 0:
        self.click = False

      WIN.blit(self.image, (self.rect.x, self.rect.y))
      return action

    

garage_button = Button(25, 525, garage_img, 0.7)

class Garage:
  def __init__(self):
    self.garageDisplay = pygame.image.load("MC_floorplan_test.jpg").convert_alpha()
    self.garageDisplay = pygame.transform.scale(self.garageDisplay, (600, 600))
  def run(self):
    run = True
    while run:
      WIN.fill((202, 228, 241))
      WIN.blit(self.garageDisplay, (0,0))

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          run = False
      pygame.display.update()

    

run = True
while run:
  WIN.fill((202, 228, 241))
  WIN.blit(cluedoMap, (0,0))

  if garage_button.draw() == True:
    GarageDisplay = Garage()
    GarageDisplay.run()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
  pygame.display.update()


pygame.quit()