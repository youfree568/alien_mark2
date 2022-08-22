import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

	def __init__(self, ai):
		super().__init__()
		self.screen = ai.screen
		self.settings = ai.settings
		self.color = self.settings.bullet_color
		# створення кулі у rect(0, 0), потім задати правильне положення
		self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
			self.settings.bullet_height)
		self.rect.midtop = ai.ship.rect.midtop
		# параметри розташування кулі в десятковому значенні
		self.y = float(self.rect.y)

	def update(self):
		"""оновити позицію кулі на екрані"""
		# оновити десяткову позицію
		self.y -= self.settings.bullet_speed
		# оновити позицію rect
		self.rect.y = self.y

	def draw_bullet(self):
		"""намалювати кулю"""
		pygame.draw.rect(self.screen, self.color, self.rect)
