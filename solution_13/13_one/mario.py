import pygame
from pygame.sprite import Sprite

class Mario(Sprite):
	def __init__(self, ma):
		super().__init__()
		self.screen = ma.screen
		# load mario image
		self.image = pygame.image.load('super_mario.bmp')
		self.rect = self.image.get_rect()
		# start each new mario near the top left of the screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		# position
		self.x = float(self.rect.x)