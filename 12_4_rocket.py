import pygame
import sys

class Rocket:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((600, 400))
		self.screen_rect = self.screen.get_rect()
		self.image = pygame.image.load('images/rocket.png')
		self.rect = self.image.get_rect()
		self.rect.center = self.screen_rect.center
		self.bg = (0, 0, 0)
		pygame.display.set_caption('ROCKET')

	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						sys.exit()
					elif event.key == pygame.K_LEFT:
						self.rect.x -= 10
					elif event.key == pygame.K_RIGHT:
						self.rect.x += 10
					elif event.key == pygame.K_UP:
						self.rect.y -= 10
					elif event.key == pygame.K_DOWN:
						self.rect.y += 10

			self.screen.fill(self.bg)
			self.blitme()
			pygame.display.flip()

	def blitme(self):
		# show rocket
		self.screen.blit(self.image, self.rect)

if __name__=='__main__':
	rock = Rocket()
	rock.run()