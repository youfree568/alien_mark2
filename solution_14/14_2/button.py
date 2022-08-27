import pygame.font

class Button:

	def __init__(self, game):
		"""initialization button atribut"""
		self.screen = game.screen
		self.screen_rect = self.screen.get_rect()
		# button settnigs
		self.button_color = (150, 150, 150)
		self.width, self.height = 400, 50
		self.text_color = (20, 20, 20)
		self.font = pygame.font.SysFont(None, 48)
		# creat button object
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center
		# message on the button must show only once
		self._prep_msg()
		# self._prep_msg_2()
		# self.message = pygame.Rect(0, 0, 150, 50)
		# self.message.center = self.screen_rect.center

	def _prep_msg(self):
		"""convert text to image"""
		self.msg_image = self.font.render('PLAY', 
			True, self.text_color, self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def draw_button(self):
		"""show button on the screen"""
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)

	# def _prep_msg_2(self):
	# 	self.msg_image2 = self.font.render('HIT', True, self.text_color, 
	# 		self.button_color)
	# 	self.msg_image2_rect = self.msg_image2.get_rect()
	# 	self.msg_image2_rect.center = self.rect.center

	# def draw_hit(self):
	# 	self.screen.fill(self.button_color, self.rect)
	# 	self.screen.blit(self.msg_image2, self.msg_image2_rect)