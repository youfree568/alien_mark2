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
		self.drop_speed = 0.2
		self._create_drop(self.screen_rect)
		self._create_fleet()

	def run(self):
		# старт програми
		while True:
			# перевіряє статус клавіш
			self.check_event()
			# визначає колір фону
			self.screen.fill(self.bg_color)
			# малює краплі на екрані
			self.drops.draw(self.screen)
			# пересуває праплі в низ
			self.fall()
			#  оновлює дощ
			self.update_rain(self)
			# відбражає останнє на екрані
			pygame.display.flip()


	def check_event(self):
		# перевірка на дію або нажаття клавіші
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
		# скільки вміщається в ряді крапель
		available_space_x = self.screen_rect.width - (drop_width * 2)
		number_drops = available_space_x // (drop_width * 2)
		# скільки рядів вміщається на екрані
		available_space_y = self.screen_rect.height - ((drop_height - 30) * 2)
		row_numbers = available_space_y // (drop_height * 2)
		# перебираємо ряди і стовбці і відображаємо на екрані
		for row_number in range(row_numbers):			
			for drop_number in range(number_drops):
				drop = Drop(self)
				drop_width, drop_height = drop.rect.size
				drop.x = drop_width + drop_width * 2 * drop_number 
				drop.rect.x = drop.x
				drop.y = drop_height + drop_height * 2 * row_number
				drop.rect.y = drop.y
				self.drops.add(drop)

	def _create_drop(self, screen_rect):
		# створюємо ряд крапель
		drop = Drop(self)
		drop_width, drop_height = drop.rect.size
		# визначення крапель в ряді
		available_space_x = self.screen_rect.width - (drop_width * 2)
		number_drops = available_space_x // (drop_width * 2)
		# визначення рядів на екрані
		available_space_y = self.screen_rect.height - ((drop_height - 30) * 2)
		row_numbers = available_space_y // (drop_height * 2)
		# перебираємо почерзі number_drops і додаємо в список
		for row_number in range(1):			
			for drop_number in range(number_drops):
				drop = Drop(self)
				drop_width, drop_height = drop.rect.size
				drop.x = drop_width + drop_width * 2 * drop_number 
				drop.rect.x = drop.x
				drop.y = (self.screen_rect.top - 50) + row_number 
				drop.rect.y = drop.y
				self.drops.add(drop)


	def fall(self):
		"""каплі падають вниз"""
		for drop in self.drops.sprites():
			drop.y += self.drop_speed
			drop.rect.y = drop.y
		

	def update_rain(self, screen_rect):
		"""видаляємо краплі що досягли низу і малюємо нові вгорі"""
		check_drope = False
		for drope in self.drops.copy():	
			if drope.rect.top >= self.screen_rect.bottom:
				self.drops.remove(drope)
				check_drope = True
		if check_drope:
			self._create_drop(self.screen_rect)
		print(len(self.drops)," крапель на екрані")


if __name__=='__main__':
	Raindrop().run()