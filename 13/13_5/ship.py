import pygame

class Ship:
	"""create ship"""
	def __init__(self, sh_game):
		self.screen = sh_game.screen
		self.image = pygame.image.load('ship2.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()
		# позиція корабля на екрані 
		self.rect.midleft = self.screen_rect.midleft
		self.y = float(self.rect.y)
		# індикатори руху корабля
		self.move_ship_up = False
		self.move_ship_down = False

	def update(self):
		"""
		update ship position and adjust if touch the land
		"""
		if self.move_ship_up and self.rect.top > 0:
			self.rect.y -= 1
		if self.move_ship_down and self.rect.bottom < self.screen_rect.bottom:
			self.rect.y += 1

	def blitme(self):
		self.screen.blit(self.image, self.rect)

	def center_ship(self):
		self.rect.midleft = self.screen_rect.midleft
		self.y = float(self.rect.y)