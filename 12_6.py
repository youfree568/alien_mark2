import pygame
import sys
from rightbullet import Bullet

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
		# move ship UP
		self.move_ship_up = False
		self.move_ship_down = False
		self.bullets = pygame.sprite.Group()


	def run(self):
		# запуск відображення програми
		while True:
			self._check_events()
			# заливаємо фон
			self.screen.fill(self.bg_color)
			# відображаємо корабель
			self.screen.blit(self.ship, self.rect)
			self.update_ship()
			# оновлення кулі
			self.bullets.update()
			# малюємо кулю
			for bullet in self.bullets.sprites():
				bullet.draw_bullet()
			# видалити кулі що дойшли верху екрану
			for bullet in self.bullets.copy():
				if bullet.rect.left > self.screen_rect.right:
					self.bullets.remove(bullet)
			print(len(self.bullets))
			# відображати екран
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


if __name__=='__main__':
	Shut_right().run()