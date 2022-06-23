import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
	"""загальний клас, що керує ресурсами та поведінкою гри"""
	def __init__(self):
		""" Ініціалізувати гру, створити ресурси гри"""
		# initialization pygame
		pygame.init()

		self.settings = Settings()
		# set window
		self.screen = pygame.display.set_mode((self.settings.screen_width, 
			self.settings.screen_height))
		# напис з назвою на верху вікна
		pygame.display.set_caption('Alien Invasion')
		self.ship = Ship(self)
		self.x = float(self.ship.rect.x)
	

	def run_game(self):
		"""start game"""
		while True:
			self._check_events()
			self._update_screen()

	def _check_events(self):
		for ev in pygame.event.get():
				# self.x = float(self.ship.rect.x)
				if ev.type == pygame.QUIT:
					sys.exit()
				elif ev.type == pygame.KEYDOWN:
					if ev.key == pygame.K_q:
						sys.exit()
					elif ev.key == pygame.K_LEFT:
						self.x -= 1
						print('move left')
					elif ev.key == pygame.K_RIGHT:
						self.x += 0.5

					self.ship.rect.x = self.x




	def _update_screen(self):
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		pygame.display.flip()

if __name__ == '__main__':
	# create copy of the game and start
	ai = AlienInvasion()
	ai.run_game()