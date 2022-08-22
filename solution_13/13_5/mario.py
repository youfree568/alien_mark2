import pygame
from pygame.sprite import Sprite

class Mario(Sprite):
	def __init__(self, ai_game):
		super().__init__()
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = ai_game.settings
		# завантажуємо зображення
		self.image = pygame.image.load('super_mario.bmp')
		self.rect = self.image.get_rect()
		
		# виставляємо позицію маріо
		self.rect.right = self.screen_rect.right - self.rect.width
		# self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		self.y = float(self.rect.y)
		

	def blitme(self):
		self.screen.blit(self.image, self.rect)

	def update(self):
		self.y += (self.settings.mario_speed * self.settings.fleet_direction)
		self.rect.y = self.y


	def check_edges(self):
		if self.rect.bottom >= self.screen_rect.bottom or self.rect.top <= 0:
			return True


