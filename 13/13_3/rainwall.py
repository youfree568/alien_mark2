import sys
import pygame

class Raindrop:
	"""створення стіни крапель яка рухається вниз"""
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((600, 480))
		pygame.display.set_caption('Raindrop')
		self.bg_color = (50, 50, 50)

	def run(self):
		while True:
			self.check_event()
			self.screen.fill(self.bg_color)
			pygame.display.flip()

	def check_event(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					sys.exit()

if __name__=='__main__':
	Raindrop().run()