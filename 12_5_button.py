import pygame
import sys

class CheckKey:
	"""here we check what button is press down"""
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((600, 400))
		pygame.display.set_caption('Check KEYDOWN')

	def run(self):
		# turn on game
		while True:
			self._check_events()
			pygame.display.flip()

	def _check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				print(pygame.key.name(event.key))

# start game
CheckKey().run()