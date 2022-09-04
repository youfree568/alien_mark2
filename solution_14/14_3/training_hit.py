import pygame
import sys
import time
from time import sleep

from settings import Settings
from rocket import Rocket
from bullet import Bullet
from target import Target
from button import Button

class Training:
	def __init__(self):
		"""training to hit target"""
		pygame.init()
		# import settings
		self.settings = Settings()
		# make screen
		# self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.screen = pygame.display.set_mode((self.settings.screen_width, 
			self.settings.screen_height))
		self.screen_rect = self.screen.get_rect()
		self.bg_color = self.settings.bg_color
		# make title name
		pygame.display.set_caption('Training')

		self.rocket = Rocket(self)
		self.bullets = pygame.sprite.Group()
		self.target = Target(self)
		self.missed = self.settings.missed_target
		self.game_status = False
		self.button = Button(self)

	def run(self):
		while True:
			"""start game move"""			
			self.check_events()
			if self.game_status == True:
				self.rocket.update()
				self.bullets.update()
				self.target.update()
				# self.levelup()			
			self.update_screen()

	def check_events(self):
		"""check events in game"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup(event)
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				self.check_play_button(mouse_pos)
				self.settings.initialization_dynamic_settings()


	def _check_keydown(self, event):
		# check if button push down
		if event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_DOWN:
			self.rocket.move_down = True
		elif event.key == pygame.K_UP:
			self.rocket.move_up = True
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()
		elif event.key == pygame.K_p:
			self.game_status = True
			self.settings.initialization_dynamic_settings()

	def out_the_target(self):
		# check and reset if shoot is out the target
		print('hit screen')
		self.missed -= 1
		if self.missed <= 0:
			self.game_status = False 
			self.missed = self.settings.missed_target
			self.bullets.empty()
			self.rocket.center()

	def levelup(self):
		# make speed faster
		if self.settings.hit_target % 10 == 0:
				self.settings.increase_speed()
		

	def _check_keyup(self, event):
		# check if button push up
		if event.key == pygame.K_DOWN:
			self.rocket.move_down = False
		elif event.key == pygame.K_UP:
			self.rocket.move_up = False

	def check_play_button(self, mouse_pos):
		# перевіряє с татус нажаття кнопки мишею
		if self.button.rect.collidepoint(mouse_pos):
			self.game_status = True

	def _fire_bullet(self):
		# контролює кількість куль на екрані
		if len(self.bullets) < self.settings.bullet_allowed:
			bullet = Bullet(self)
			self.bullets.add(bullet)

	def _update_bullet(self):
		coli = pygame.sprite.spritecollide(self.target, self.bullets, True)
		# self.hit_target += 1
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		for bullet in self.bullets.copy():
			if bullet.rect.left >= self.screen_rect.right:
				self.bullets.remove(bullet)
				self.out_the_target()
		if coli:
			self.settings.hit_target += 1
			# sleep(0.2)		
			print(self.settings.hit_target)
			self.levelup()
		# pygame.sprite.spritecollide(self.target, self.bullets, True)

	def _update_target_direction(self):
		if self.target.check_edges():
			self.settings.target_direction *= -1

	def update_screen(self):
		"""update screen"""
		self.screen.fill(self.bg_color)
		self.rocket.blitmi()
		self._update_bullet()
		self.target.draw_target()
		self._update_target_direction()
		if self.game_status == False:
			self.button.draw_button()

		pygame.display.flip()

if __name__=='__main__':
	Training().run()