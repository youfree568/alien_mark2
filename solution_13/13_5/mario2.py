import pygame
from pygame.sprite import Sprite

class Marioo(Sprite):
	def __init__(self, main):
		super().__init__()
		self.screen = main.screen

		self.image = pygame.image.load('super_mario.bmp')
		self.rect = self.image.get_rect()

		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

