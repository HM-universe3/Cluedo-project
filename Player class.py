import pygame
class Player():
  def __init__(self, x, y, width, height, colour):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.colour = colour
    self.rect = (self.x,self.y,self.width,self.height)
    self.vel = 0.5
  def draw(self, win):
    pygame.draw.rect(win, self.colour, self.rect)

  def move(self):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
      self.x -= self.vel
    
    if keys[pygame.K_RIGHT]:
      self.x += self.vel
    
    if keys[pygame.K_UP]:
      self.y -= self.vel
    
    if keys[pygame.K_DOWN]:
      self.y += self.vel

    self.rect = (self.x,self.y,self.width,self.height)
