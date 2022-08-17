import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
	"""створення кулі"""
	def __init__(self, ai):
		super().__init__()
		self.screen = ai.screen
		self.settings = ai.settings
		self.color = self.settings.bullet_color
		self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
		self.rect.midleft = ai.ship.rect.midright
		self.x = float(self.rect.x)

	def update(self):
		# update bullet possition
		self.x += self.settings.bullet_speed
		self.rect.x = self.x

	def draw_bullet(self):
		# show bullet
		pygame.draw.rect(self.screen, self.settings.bullet_color, self.rect)