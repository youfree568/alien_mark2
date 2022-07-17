import pygame
import sys
from mario import Mario
from random import randint

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
		mario_width, mario_height = mario.rect.size
		# кількість в ряді
		available_space_x = self.screen_rect.width - (2 * mario_width)
		number_marios_x = available_space_x // (2 * mario_width)
		# кількість рядів
		available_space_y = self.screen_rect.height - mario_height
		number_rows = available_space_y // (2 * mario_height)
		# перебираємо і виводимо на екран маріо
		for row in range(number_rows):
			# пребираємо який ряд
			for mario_number in range(number_marios_x):
				# перебираємо кількість в ряді
				# задаємо параметри маріо, шир. вис. 
				mario = Mario(self)
				# рандомне значення
				random_place = randint(-20, 20)
				# позиція кожного маріо в ряді
				mario.x = mario_width + 2 * mario_width * mario_number + random_place
				mario.rect.x = mario.x
				# позиція ряду на екрані				
				mario.y = mario_height + 2 * mario_height * row + random_place
				mario.rect.y = mario.y
				self.marios.add(mario)
	

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