import pygame
from pygame.sprite import Sprite

class Drop(Sprite):
	"""make drop"""
	def __init__(self, drop_game):
		super().__init__()
		self.screen = drop_game.screen
		# load image
		self.image = pygame.image.load('drop.bmp')
		self.rect = self.image.get_rect()
		# start each drop the top left of the screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		# позиція крапель по осі х
		self.x = float(self.rect.x)