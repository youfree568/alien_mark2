import pygame
import sys

class Shut_right:
	def __init__(self):
		pygame.init()
		# розміри екрану
		self.screen = pygame.display.set_mode((640, 480))
		# rect екрану
		self.screen_rect = self.screen.get_rect()
		# колір фону
		self.bg_color = (230, 230, 230)
		pygame.display.set_caption("SHIP SHUT RIGHT")
		# додаємо зображення корабля
		self.ship = pygame.image.load('images/ship2.bmp')
		# рект корабля
		self.rect = self.ship.get_rect()
		# положення корабля
		self.rect.midleft = self.screen_rect.midleft

	def run(self):
		# запуск відображення програми
		while True:
			self._check_events()
			# заливаємо фон
			self.screen.fill(self.bg_color)
			# відображаємо корабель
			self.screen.blit(self.ship, self.rect)
			# відображати екран
			pygame.display.flip()

	def _check_events(self):
		# перевіряємо події
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					self.rect.y -= 5
				if event.key == pygame.K_DOWN:
					self.rect.y += 5
				# вихід з гри
				if event.key == pygame.K_q:
					sys.exit()

if __name__=='__main__':
	Shut_right().run()