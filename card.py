import pygame

class Card:
  def __init__(self, cardName, cardImage):
    self.name = cardName
    self.imagePath = str(cardImage).jpg
    self.image = pygame.image.load(self.imagePath)
