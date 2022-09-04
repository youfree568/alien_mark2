import pygame.font

class Button:

	def __init__(self, game):
		"""initialization button atribut"""
		self.screen = game.screen
		self.screen_rect = self.screen.get_rect()
		# button settnigs
		self.button_color1 = (10, 150, 10)
		self.button_color2 = (150, 10, 10)
		self.width, self.height = 150, 50
		self.text_color = (20, 20, 20)
		self.font = pygame.font.SysFont(None, 48)
		# creat button object
		self.rect1 = pygame.Rect(0, 0, self.width, self.height)
		self.rect1.midbottom = self.screen_rect.center

		self.rect2 = pygame.Rect(0, 0, self.width, self.height)
		self.rect2.midtop = self.screen_rect.center
		# message on the button must show only once
		self._prep_msg1()
		self._prep_msg2()
		# self.message = pygame.Rect(0, 0, 150, 50)
		# self.message.center = self.screen_rect.center

	def _prep_msg1(self):
		"""convert text to image"""
		self.msg_image1 = self.font.render('EASY', 
			True, self.text_color, self.button_color1)
		self.msg_image_rect1 = self.msg_image1.get_rect()
		self.msg_image_rect1.center = self.rect1.center

	def _prep_msg2(self):
		"""convert text to image"""
		self.msg_image2 = self.font.render('HARD', 
			True, self.text_color, self.button_color2)
		self.msg_image_rect2 = self.msg_image2.get_rect()
		self.msg_image_rect2.center = self.rect2.center


	def draw_button1(self):
		"""show button on the screen"""
		self.screen.fill(self.button_color1, self.rect1)
		self.screen.blit(self.msg_image1, self.msg_image_rect1)

	def draw_button2(self):
		self.screen.fill(self.button_color2, self.rect2)
		self.screen.blit(self.msg_image2, self.msg_image_rect2)

	# def _prep_msg_2(self):
	# 	self.msg_image2 = self.font.render('HIT', True, self.text_color, 
	# 		self.button_color)
	# 	self.msg_image2_rect = self.msg_image2.get_rect()
	# 	self.msg_image2_rect.center = self.rect.center

	# def draw_hit(self):
	# 	self.screen.fill(self.button_color, self.rect)
	# 	self.screen.blit(self.msg_image2, self.msg_image2_rect)