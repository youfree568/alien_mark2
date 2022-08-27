import pygame

class Target:

	def __init__(self, game):
		self.screen = game.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = game.settings
		self.rect = pygame.Rect(0, 0, self.settings.target_width, 
			self.settings.target_height)
		self.rect.center = self.screen_rect.center
		self.y = float(self.rect.y)
		self.change_direction = self.settings.target_direction

	def draw_target(self):
		pygame.draw.rect(self.screen, self.settings.target_color, 
			self.rect)

	def update(self):
		self.y += (self.settings.target_speed * self.settings.target_direction)
		self.rect.y = self.y

	def check_edges(self):
		screen_rect = self.screen_rect
		if self.rect.bottom >= self.screen_rect.bottom or self.rect.top <= 0:
			return True
