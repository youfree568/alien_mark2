import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""створення кулі"""
	def __init__(self, ai):
		super().__init__()
		self.screen = ai.screen
		self.ship = ai.ship
		# create bullet
		self.bullet_width = 15
		self.bullet_height = 3
		self.bullet_color = (60, 60, 60)
		self.bullet_speed = 0.05
		self.rect = pygame.Rect(0, 0, self.bullet_width, self.bullet_height)
		self.rect.midleft = ai.rect.midright
		self.x = float(self.rect.x)

	def update(self):
		self.x += self.bullet_speed
		self.rect.x = self.x

		

	def draw_bullet(self):
		pygame.draw.rect(self.screen, self.bullet_color, self.rect)