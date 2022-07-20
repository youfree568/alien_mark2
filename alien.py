import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""клас що створює прибульця"""
	def __init__(self, ai):
		super().__init__()
		self.screen = ai.screen
		self.settings = ai.settings
		# load image
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()
		# start each new alien on the top left of the screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		# Store the alien's exact horizontal position
		self.x = float(self.rect.x)

