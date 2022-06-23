import pygame
import sys


# # робимо синій фон тільки з допомогою функції
# def run():
# 	pygame.init()
# 	screen = pygame.display.set_mode((600, 400))
	# pygame.display.set_caption('home_work_12-1')

# 	while True:
# 		for e in pygame.event.get():
# 			if e.type == pygame.QUIT:
# 				sys.exit()
# 		screen.fill((0, 0, 250))
# 		pygame.display.flip()

# run()

# робимо фон з допомогою класів
class Main:
	def __init__(self):			
		pygame.init()
		self.screen = pygame.display.set_mode((600, 400))
		pygame.display.set_caption('home_work_12-1')
		self.bg_color = (0, 0, 250)
	def run(self):
		while True:
			for e in pygame.event.get():
				if e.type == pygame.QUIT:
					sys.exit()
			self.screen.fill(self.bg_color)
			pygame.display.flip()
# 
# запускає через виклик класу і функції
# Main().run()

# запускає якщо файл викликався напряму
if __name__=='__main__':
	Main().run()