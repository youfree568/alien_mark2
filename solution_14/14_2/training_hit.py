import pygame
import sys
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
		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.screen_rect = self.screen.get_rect()
		self.bg_color = self.settings.bg_color
		# make title name
		pygame.display.set_caption('Training')

		self.rocket = Rocket(self)
		self.bullets = pygame.sprite.Group()
		self.target = Target(self)
		self.missed_target = 10
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

	def _check_keyup(self, event):
		# check if button push up
		if event.key == pygame.K_DOWN:
			self.rocket.move_down = False
		elif event.key == pygame.K_UP:
			self.rocket.move_up = False

	def check_play_button(self, mouse_pos):
		if self.button.rect.collidepoint(mouse_pos):
			self.game_status = True

	def _fire_bullet(self):
		if len(self.bullets) < self.settings.bullet_allowed:
			bullet = Bullet(self)
			self.bullets.add(bullet)

	def _update_bullet(self):
		coli = pygame.sprite.spritecollide(self.target, self.bullets, True)
		
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		for bullet in self.bullets.copy():
			if bullet.rect.left >= self.screen_rect.right:
				self.bullets.remove(bullet)
				print('hit screen')
				self.missed_target -= 1
				if self.missed_target <= 0:
					self.game_status = False 
					self.missed_target = 3
					self.bullets.empty()
					self.rocket.center()
		if coli:
			sleep(0.2)				
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