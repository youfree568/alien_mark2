import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
	"""загальний клас, що керує ресурсами та поведінкою гри"""
	def __init__(self):
		""" Ініціалізувати гру, створити ресурси гри"""
		# initialization pygame
		pygame.init()

		self.settings = Settings()
		# set window
		# self.screen = pygame.display.set_mode((self.settings.screen_width, 
			# self.settings.screen_height))
		# make full screen
		self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		# напис з назвою на верху вікна
		pygame.display.set_caption('Alien Invasion')
		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()
		
		self._create_fleet()

	def run_game(self):
		"""start game"""
		while True:
			self._check_events()
			self.ship.update()
			self._update_bullets()
			
			self._update_screen()

	def _check_events(self):
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				sys.exit()
			elif e.type == pygame.KEYDOWN:
				self._check_events_keydown(e)
			elif e.type == pygame.KEYUP:
				self._check_events_keyup(e)

	def _check_events_keydown(self, e):
		# реакція на натиснуту клавішу
		if e.key == pygame.K_RIGHT:
			self.ship.moving_right = True
		elif e.key == pygame.K_LEFT:
			self.ship.moving_left = True
		elif e.key == pygame.K_SPACE:
			self._fire_bullet()			
		elif e.key == pygame.K_q:
			sys.exit()

	def _check_events_keyup(self, e):
		# реакція на ненатиснуту клавішу
		if e.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif e.key == pygame.K_LEFT:
			self.ship.moving_left = False

	def _update_screen(self):
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		self._show_bullets()
		self.aliens.draw(self.screen)
		pygame.display.flip()

	def _show_bullets(self):
		# відображає по черзі випущені кулі
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()

	def _fire_bullet(self):
		# додає кулі у список
		if len(self.bullets) < self.settings.bullet_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _remove_bullet(self):
		# видаляє кулі що досягнули верху екрану
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <=0:
				self.bullets.remove(bullet)		

	def _update_bullets(self):
		"""оновити позицію кулі і видалити стару"""
		# оновити позиції куль
		self.bullets.update()
		# видалити старукую
		self._remove_bullet()

	def _create_fleet(self):
		"""створення флоту прибульців"""
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		ship_height = self.ship.rect.height
		# визначаємо кількість прибульців що поміститься в ряд на екрані
		available_space_x = self.settings.screen_width - (alien_width * 2)
		number_alien_x = available_space_x // (alien_width * 2)
		# визначаємо кількість рядів рибульців
		available_space_y = self.settings.screen_height - (alien_height * 3) - ship_height
		number_rows = available_space_y // (alien_height * 2)
		for row in range(number_rows):
			# create the first row of aliens
			for alien_number in range(number_alien_x):
				self._create_alien(alien_number, row)

	def _create_alien(self, alien_number, row):
		"""create an alien and place it in a row"""
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		alien.x = alien_width + alien_width * 2 * alien_number
		alien.rect.x = alien.x
		alien.y = alien_height + alien_height * 2 * row
		alien.rect.y = alien.y
		self.aliens.add(alien)


if __name__ == '__main__':
	# create copy of the game and start
	ai = AlienInvasion()
	ai.run_game()