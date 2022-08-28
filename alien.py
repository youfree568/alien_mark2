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

	def update(self):
		"""змістити прибульця праворуч""" 
		self.x += self.settings.alien_speed * self.settings.fleet_direction
		self.rect.x = self.x
		self.check_edges()

	def check_edges(self):
		self.screen_rect = self.screen.get_rect()
		if self.rect.right >= self.screen_rect.right or self.rect.left <= 0:
			return True