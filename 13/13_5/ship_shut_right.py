import pygame
import sys

from time import sleep

from settings import Settings
from ship import Ship
from bullet import Bullet
from mario import Mario
from game_stats import GameStats

class Shut_right:
	def __init__(self):
		pygame.init()
		# розміри екрану
		self.settings = Settings()
		self.screen = pygame.display.set_mode((self.settings.screen_width, 
			self.settings.screen_height))
		# rect екрану
		self.screen_rect = self.screen.get_rect()
		pygame.display.set_caption("SHIP SHUT RIGHT")
		
		self.stats = GameStats(self)
		self.ship = Ship(self)		
		self.bullets = pygame.sprite.Group()
		self.marios = pygame.sprite.Group()
		self.collis = pygame.sprite.Group()
		self._create_fleet()

	def run(self):
		""" запуск відображення програми"""
		while True:
			self._check_events()
			if self.stats.game_active:
				self.ship.update()
				self._update_bullet()
				self._update_marios()
			self._update_screen()
			
	def _check_events(self):
		# перевіряємо події
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup(event)

	def _check_keydown(self, event):
		if event.key == pygame.K_UP:
			self.ship.move_ship_up = True
		if event.key == pygame.K_DOWN:
			self.ship.move_ship_down = True
		if event.key == pygame.K_SPACE:
			# випускати кулю
			self._fire_bullet()
		# вихід з гри
		if event.key == pygame.K_q:
			sys.exit()

	def _check_keyup(self, event):
		"""check if key up"""
		if event.key == pygame.K_UP:
			self.ship.move_ship_up = False
		if event.key == pygame.K_DOWN:
			self.ship.move_ship_down = False

	def _fire_bullet(self):
		"""add bullet to list"""
		if len(self.bullets) < 4:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _update_bullet(self):
		self.bullets.update()
		# remove bullet from the screen
		for bullet in self.bullets.copy():
			if bullet.rect.right > self.screen_rect.right:
				self.bullets.remove(bullet)
		self._bullet_mario_collision()

	def _bullet_mario_collision(self):
		"""реакція на зіткнення кулі і маріо """
		# remove all bullets and marios that were hit
		collisions = pygame.sprite.groupcollide(self.bullets, self.marios,
			True, True)
		self.collis.add(collisions)
		# print(len(self.collis))
		if len(self.collis) >= 1:
			print('More than 100 marios hit.\nYou win!')
		
			self.stats.game_active = False
		if not self.marios:
			# remove bullet and create marios fleet
			self.bullets.empty()
			self._create_fleet()
	
	def _update_marios(self):
		"""оновити позиції всіх маріо"""
		self._check_fleet_edges()
		self.marios.update()
		# перевірити чи не зіткнулись маріо з кораблем
		if pygame.sprite.spritecollideany(self.ship, self.marios):
			self._ship_hit()

		self._check_marios_left()

	def _update_screen(self):
		"""оновити зображення та перемкнутися на новий екран"""
		self.screen.fill(self.settings.bg_color)
		# відображаємо корабель		
		self.ship.blitme()
		# відображення кулі
		for bullet in self.bullets.sprites():
				bullet.draw_bullet()
		# print(len(self.bullets))
		# print(len(self.marios))
		self.marios.draw(self.screen)

		pygame.display.flip()


	def _create_fleet(self):
		"""create fleet of marios"""
		# create mario
		mario = Mario(self)
		mario_width, mario_height = mario.rect.size
		# find how many marios go to the screen
		available_space_y = self.screen_rect.height - (mario_height * 2)
		number_marios_y = available_space_y // (mario_height * 2)
		available_space_x = self.screen_rect.width - (mario_width * 2) - self.ship.rect.width * 4
		number_marios_x = available_space_x // (mario_width * 2)
		# add mario on rows and
		for row_mario in range(number_marios_x):
			for mario_number in range(number_marios_y):
				self._create_mario(mario_number, row_mario)


	def _create_mario(self, mario_number, row_mario):
		mario = Mario(self)
		mario_width, mario_height = mario.rect.size
		mario.y = mario_height + (2 * mario_height) * mario_number
		mario.x = (2 * mario_width) * row_mario + self.ship.rect.width * 6
		mario.rect.y = mario.y
		mario.rect.x = mario.x
		self.marios.add(mario)

	def _check_fleet_edges(self):
		for mario in self.marios.sprites():
			if mario.check_edges():
				self._change_fleet_direction()
				break

	def _change_fleet_direction(self):
		#зміна напрямку руху флоту
		for mario in self.marios.sprites():
			mario.rect.x -= self.settings.fleet_drop_speed
		self.settings.fleet_direction *= -1

	def _ship_hit(self):
		"""reaction to ship hit"""
		if self.stats.ships_left > 0:
			self.stats.ships_left -= 1
			# clear bullet and marios
			self.bullets.empty()
			self.marios.empty()
			# create fleet and center ship
			self._create_fleet()
			self.ship.center_ship()
			# timer to watch hit
			sleep(0.5)
		else:
			self.stats.game_active = False

	def _check_marios_left(self):
		# check if mario has touched the edge of the screen
		for mario in self.marios.sprites():
			if mario.rect.left <= 0:
				self._ship_hit()
				break

if __name__=='__main__':
	Shut_right().run()