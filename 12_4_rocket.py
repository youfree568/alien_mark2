import pygame
import sys

class Rocket:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
		# self.screen_width = self.screen.get_rect().width
		# self.screen_height = self.screen.get_rect().height
		self.screen_rect = self.screen.get_rect()
		self.image = pygame.image.load('images/rocket.png')
		self.rect = self.image.get_rect()
		self.rect.center = self.screen_rect.center
		self.bg = (0, 0, 0)
		self.move_left = False
		self.move_right = False
		self.move_up = False
		self.move_down = False
		self.speed = 3
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)
		pygame.display.set_caption('ROCKET')

	def run(self):
		while True:
			# перевіряє натискання клавіш
			self._check_events()
			# заливає фон
			self.screen.fill(self.bg)
			# рухає ракетою
			self._update_move()
			# малює ракету
			self.blitme()
			# показує останній екран
			pygame.display.flip()

	def _check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown(event)				
			elif event.type == pygame.KEYUP:
				self._check_keyup()

	def _check_keydown(self, event):
		if event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_LEFT:
			self.move_left = True
		elif event.key == pygame.K_RIGHT:
			self.move_right = True
		elif event.key == pygame.K_UP:
			self.move_up = True
		elif event.key == pygame.K_DOWN:
			self.move_down = True

	def _check_keyup(self):
		self.move_left = False
		self.move_right = False
		self.move_up = False
		self.move_down = False

	def _update_move(self):
		if self.move_left and self.rect.left + 24 > 0:
			self.x -= self.speed
		if self.move_right and self.rect.right - 24 < self.screen_rect.right:
			self.x += self.speed
		if self.move_up and self.rect.top > 0:
			self.y -= self.speed
		if self.move_down and self.rect.bottom < self.screen_rect.bottom:
			self.y += self.speed

		self.rect.x = self.x
		self.rect.y = self.y

	def blitme(self):
		# show rocket
		self.screen.blit(self.image, self.rect)

if __name__=='__main__':
	rock = Rocket()
	rock.run()