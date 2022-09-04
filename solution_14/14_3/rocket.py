import pygame

class Rocket:
	"""make rocket, whit her, we will be training"""
	def __init__(self, game):

		self.screen = game.screen
		self.settings = game.settings
		self.screen_rect = self.screen.get_rect()
		# add ship
		self.image = pygame.image.load('rocket.png')
		self.rect = self.image.get_rect()
		self.rect.midleft = self.screen_rect.midleft
		# move ship 
		self.move_up = False
		self.move_down = False

		self.y = float(self.rect.y)

	def blitmi(self):
		# show ship
		self.screen.blit(self.image, self.rect)

	def update(self):
		# move ship
		if self.move_down and self.rect.bottom < self.screen_rect.bottom:
			self.y += self.settings.ship_speed
		if self.move_up and self.rect.top > 0:
			self.y -= self.settings.ship_speed
		self.rect.y = self.y

	def center(self):
		self.rect.midleft = self.screen_rect.midleft
		self.y = float(self.rect.y)