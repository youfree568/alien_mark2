import pygame
import sys

class CheckKey:
	"""here we check what button is press down and show it on the screen"""
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((600, 400))
		self.screen_rect = self.screen.get_rect()
		self.bg_color = (0, 50, 50)
		pygame.display.set_caption('Check KEYDOWN')
		# параметри тексту
		self.font = pygame.font.Font('freesansbold.ttf', 40)
		self.on = 'Hello'
		# з атрибутами .font.renger не розбирався
		self.text = self.font.render(self.on ,True, (230, 230, 100))
		# беремо рект тексту і позиціонуємо
		self.textRect = self.text.get_rect()
		self.textRect.center = self.screen_rect.center

	def _check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				# перевіряємо яка клавіша нажата
				self.on = pygame.key.name(event.key)
				self.text = self.font.render(self.on ,True, (230, 230, 230))

	def run(self):
		# turn on game
		while True:
			# перевірка клавіші
			self._check_events()
			# вивід фону
			self.screen.fill(self.bg_color)
			# вивід тексту
			self.screen.blit(self.text, self.textRect)
			pygame.display.flip()


# start game
CheckKey().run()