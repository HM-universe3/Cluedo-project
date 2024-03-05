import pygame, sys
from pygame.locals import QUIT

WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cluedo")
cluedoMap = pygame.image.load('Cluedo map.png').convert_alpha()
cluedoBoard = pygame.transform.scale(cluedoMap, (600, 600))
mouse = pygame.mouse.get_pos()


garage_img = pygame.image.load("garage_button.png").convert_alpha()
dining_img = pygame.image.load("button_dining-room.png").convert_alpha()
bathroom_img = pygame.image.load("button_bathroom.png").convert_alpha()
bedroom_img = pygame.image.load("button_bedroom.png").convert_alpha()
greenhouse_img = pygame.image.load("button_greenhouse.png").convert_alpha()
living_img = pygame.image.load("button_living-room.png").convert_alpha()
office_img = pygame.image.load("button_office.png").convert_alpha()
hall_img = pygame.image.load("button_hallway.png").convert_alpha()
fountain_img = pygame.image.load("button_fountain.png").convert_alpha()


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

    
#make buttons
garage_button = Button(25, 525, garage_img, 0.7)
dining_button = Button(20, 275, dining_img, 0.6)
bath_button = Button(205, 60, bathroom_img, 0.6)
bed_button = Button(25, 60, bedroom_img, 0.7)
greenH_button = Button(430, 500, greenhouse_img, 0.7)
living_button = Button(430, 275, living_img, 0.7)
office_button = Button(430, 60, office_img, 0.7)
hall_button = Button(20, 140, hall_img, 0.7)
fountain_button = Button(235, 375, fountain_img, 0.7)

class Garage:
  def __init__(self):
    self.garageDisplay = pygame.image.load("Garage image.png").convert_alpha()
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

class DiningRoom:
  def __init__(self):
    self.DiningRoomDisplay = pygame.image.load("Dining room image.png")#insert image here
    self.DiningRoomDisplay = pygame.transform.scale(self.DiningRoomDisplay, (600, 600))
  
  def run(self):
    run = True
    while run:
      WIN.fill((202, 228, 241))
      WIN.blit(self.DiningRoomDisplay, (0,0))

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          run = False
      pygame.display.update()


class Bedroom:
  def __init__(self):
    self.BedroomDisplay = pygame.image.load("Bedroom image.png")#insert image here
    self.BedroomDisplay = pygame.transform.scale(self.BedroomDisplay, (600, 600))
  def run(self):
    run = True
    while run:
      WIN.fill((202, 228, 241))
      WIN.blit(self.BedroomDisplay, (0,0))

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          run = False
      pygame.display.update()
  
class Hallway:
  def __init__(self):
    self.HallwayDisplay = pygame.image.load("Hallway image.png")#insert image here
    self.HallwayDisplay = pygame.transform.scale(self.HallwayDisplay, (600, 600))
  
  def run(self):
    run = True
    while run:
      WIN.fill((202, 228, 241))
      WIN.blit(self.HallwayDisplay, (0,0))

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          run = False
      pygame.display.update()

class Office:
  def __init__(self):
    self.OfficeDisplay = pygame.image.load("Office image.png")#insert image here
    self.OfficeDisplay = pygame.transform.scale(self.OfficeDisplay, (600, 600))
  def run(self):
    run = True
    while run:
      WIN.fill((202, 228, 241))
      WIN.blit(self.OfficeDisplay, (0,0))

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          run = False
      pygame.display.update()

  
class Bathroom:
  def __init__(self):
    self.BathroomDisplay = pygame.image.load("Bathroom image.png")#insert image here
    self.BathroomDisplay = pygame.transform.scale(self.BathroomDisplay, (600, 600))
  def run(self):
    run = True
    while run:
      WIN.fill((202, 228, 241))
      WIN.blit(self.BathroomDisplay, (0,0))

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          run = False
      pygame.display.update()

class LivingRoom:
  def __init__(self):
    self.LivingRoomDisplay = pygame.image.load("Living room image.png")#insert image here
    self.LivingRoomDisplay = pygame.transform.scale(self.LivingRoomDisplay, (600, 600))
  def run(self):
    run = True
    while run:
      WIN.fill((202, 228, 241))
      WIN.blit(self.LivingRoomDisplay, (0,0))

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          run = False
      pygame.display.update()

class GreenHouse:
  def __init__(self):
    self.GreenHouseDisplay = pygame.image.load("Greenhouse image.png")#insert image here
    self.GreenHouseDisplay = pygame.transform.scale(self.GreenHouseDisplay, (600, 600))
  def run(self):
    run = True
    while run:
      WIN.fill((202, 228, 241))
      WIN.blit(self.GreenHouseDisplay, (0,0))

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          run = False
      pygame.display.update()

class Fountain:
  def __init__(self):
    self.FountainDisplay = pygame.image.load("Fountain image.png")#insert image here
    self.FountainDisplay = pygame.transform.scale(self.FountainDisplay, (600, 600))
  def run(self):
    run = True
    while run:
      WIN.fill((202, 228, 241))
      WIN.blit(self.FountainDisplay, (0,0))

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          run = False
      pygame.display.update()
    


run = True
while run:
  WIN.fill((202, 228, 241))
  WIN.blit(cluedoBoard, (0,0))

  if garage_button.draw() == True:
    GarageDisplay = Garage()
    GarageDisplay.run()

  if dining_button.draw() == True:
    DiningDisplay = DiningRoom()
    DiningDisplay.run()

  if bath_button.draw() == True:
    BathDisplay = Bathroom()
    BathDisplay.run()

  if bed_button.draw() == True:
    BedDisplay = Bedroom()
    BedDisplay.run()

  if greenH_button.draw() == True:
    GreenDisplay = GreenHouse()
    GreenDisplay.run()

  if living_button.draw() == True:
    livingDisplay = LivingRoom()
    livingDisplay.run()

  if office_button.draw() == True:
    officeDisplay = Office()
    officeDisplay.run()

  if hall_button.draw() == True:
    hallDisplay = Hallway()
    hallDisplay.run()

  if fountain_button.draw() == True:
    fountainDisplay = Fountain()
    fountainDisplay.run()

for event in pygame.event.get():
  if event.type == pygame.QUIT:
    run = False
pygame.display.update()


pygame.quit()
