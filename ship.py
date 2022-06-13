import pygame

class Ship:
	"""make ship"""
	def __init__(self, game):
		self.screen = game.screen
		self.screen_rect = game.screen.get_rect()

		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.rect.midbottom = self.screen_rect.midbottom

	def blitme(self):
		self.screen.blit(self.image, self.rect)
		# додай зображення корабля
		# визнач рект екрану та корабля
		# зпозиціоную корабель на екрані