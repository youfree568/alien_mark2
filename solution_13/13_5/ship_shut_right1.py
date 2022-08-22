import pygame
import sys
from bullet import Bullet
from mario import Mario

class Shut_right:
	def __init__(self):
		pygame.init()
		# розміри екрану
		self.screen = pygame.display.set_mode((1200, 600))
		# rect екрану
		self.screen_rect = self.screen.get_rect()
		# колір фону
		self.bg_color = (230, 230, 230)
		pygame.display.set_caption("SHIP SHUT RIGHT")
		# додаємо зображення корабля
		self.ship = pygame.image.load('ship2.bmp')
		# рект корабля
		self.rect = self.ship.get_rect()
		# положення корабля
		self.rect.midleft = self.screen_rect.midleft
		# move ship UP
		self.move_ship_up = False
		self.move_ship_down = False
		self.bullets = pygame.sprite.Group()
		self.marios = pygame.sprite.Group()
		self._create_fleet()

		# mario = Mario(self)
		# mario_height = mario.rect.height
		# self.marios.add(mario)
		# available_space_y = self.screen_rect.height - (mario_height * 2)
		# number_marios_y = available_space_y // (mario_height * 2)
		# self._create_fleet()



	def run(self):
		# запуск відображення програми
		# available_space_x = self.screen_rect.width - (mario_width * 2) + self.rect.width
		# number_marios_x = available_space_x // (mario_width * 2)
		# print(number_marios_y)

		while True:
			self._check_events()
			self.update_ship()		

			# оновлення кулі
			self.bullets.update()
			for bullet in self.bullets.copy():
				if bullet.rect.left >= self.screen_rect.right:
					self.bullets.remove(bullet)

			self.screen.fill(self.bg_color)
			# відображаємо корабель
			self.screen.blit(self.ship, self.rect)
			# self.mario.blitme()
			for bullet in self.bullets.sprites():
					bullet.draw_bullet()

			self.marios.draw(self.screen)
			print(len(self.marios))
			# print(len(self.bullets))
			pygame.display.flip()	
			

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
			self.move_ship_up = True
		if event.key == pygame.K_DOWN:
			self.move_ship_down = True
		if event.key == pygame.K_SPACE:
			# випускати кулю
			self._fire_bullet()
		# вихід з гри
		if event.key == pygame.K_q:
			sys.exit()


	def _check_keyup(self, event):
		if event.key == pygame.K_UP:
			self.move_ship_up = False
		if event.key == pygame.K_DOWN:
			self.move_ship_down = False


	def update_ship(self):
		if self.move_ship_up and self.rect.top > 0:
			self.rect.y -= 1
		if self.move_ship_down and self.rect.bottom < self.screen_rect.bottom:
			self.rect.y += 1


	def _fire_bullet(self):
		if len(self.bullets) < 3:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)


	def _create_fleet(self):
		mario = Mario(self)
		mario_height = mario.rect.height
		available_space_y = self.screen_rect.height - (2 *mario_height)
		number_marios_y = available_space_y // (2 * mario_height)


		# for row_mario in range(number_marios_x): 

		for mario_number in range(number_marios_y):
			mario = Mario(self)
			mario_height = mario.rect.height
			mario.y = mario_height + (2 * mario_height) * mario_number
			# mario.rect.x = mario_width + (2 * mario_width) * row_mario
			mario.rect.y = mario.y
			self.marios.add(mario)

	def update_screen(self):
		self.screen.fill(self.bg_color)
		# відображаємо корабель
		self.screen.blit(self.ship, self.rect)
		for bullet in self.bullets.sprites():
				bullet.draw_bullet()
		print(len(self.bullets))
		pygame.display.flip()




if __name__=='__main__':

	Shut_right().run()