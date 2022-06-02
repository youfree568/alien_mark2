import sys

import pygame

class AlienInvasion:
	"""загальний клас, що керує ресурсами та поведінкою гри"""
	def __init__(self):
		""" Ініціалізувати гру, створити ресурси гри"""
		# initialization pygame
		pygame.init()
		# set window
		self.screen = pygame.display.set_mode((600, 400))
		# напис з назвою на верху вікна
		pygame.display.set_caption('Alien Invasion')

	def run_game(self):
		"""start game"""
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

			pygame.display.flip()


if __name__ == '__main__':
	# create copy of the game and start
	ai = AlienInvasion()
	ai.run_game()