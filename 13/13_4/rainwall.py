import sys
import pygame
from pygame.sprite import Sprite
from drop import Drop

class Raindrop(Sprite):
	"""створення стіни крапель яка рухається вниз"""
	def __init__(self):
		super().__init__()
		pygame.init()
		self.screen = pygame.display.set_mode((600, 480))
		pygame.display.set_caption('Raindrop')
		self.bg_color = (240, 240, 240)


		self.drops = pygame.sprite.Group()
		self.screen_rect = self.screen.get_rect()
		
		self.drops = pygame.sprite.Group()

		self._create_fleet()

	def run(self):
		# старт програми
		while True:
			self.check_event()
			self.screen.fill(self.bg_color)
			self._create_fleet()
			self.drops.draw(self.screen)

			pygame.display.flip()

	def le(self):
		print(len(self.drops))

	def check_event(self):
		# перевірка на дію
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					sys.exit()

	def _create_fleet(self):
		"""create rain"""
		# create drop
		drop = Drop(self)
		drop_width, drop_height = drop.rect.size

		available_space_x = self.screen_rect.width - (drop_width * 2)
		number_drops = available_space_x // (drop_width * 2)

		available_space_y = self.screen_rect.height - ((drop_height - 30) * 2)
		row_numbers = available_space_y // (drop_height * 2)
		# перебираємо почерзі number_drops і додаємо в список
		for row_number in range(row_numbers):			
			for drop_number in range(number_drops):
				drop = Drop(self)
				drop.x = drop_width + drop_width * 2 * drop_number 
				drop.rect.x = drop.x
				drop.y = drop_height + drop_height * 2 * row_number
				drop.rect.y = drop.y
				self.drops.add(drop)





if __name__=='__main__':
	Raindrop().run()
	Raindrop().le()


	# def move_drop(self):
