import pygame
import sys
from mario import Mario

class Marios():
	"""make a fleet of marios"""
	def __init__(self):
		"""make screen and fleet"""
		pygame.init()
		self.screen = pygame.display.set_mode((640, 480))
		self.screen_rect = self.screen.get_rect()
		pygame.display.set_caption('Stars')
		self.bg_color = (250, 250, 250)	
		self.marios = pygame.sprite.Group()

		# add mario on screen
		mario = Mario(self)
		mario_width = mario.rect.width
		available_space_x = self.screen_rect.width - (2 * mario_width)
		number_marios_x = available_space_x // (2 * mario_width)
		# перебираємо і виводимо на екран маріо
		for mario_number in range(number_marios_x):
			mario = Mario(self)
			mario.x = mario_width + 2 * mario_width * mario_number
			mario.rect.x = mario.x
			self.marios.add(mario)

			print(mario_number)
	

	def run_game(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
			self.screen.fill(self.bg_color)
			self.marios.draw(self.screen)
			pygame.display.flip()

if __name__=='__main__':
	Marios().run_game()