import pygame.font

class Button:
	def __init__(self, ai, msg):
		self.screen = ai.screen
		self.screen_rect = self.screen.get_rect()
		# size and font button
		self.width, self.height = 200, 50
		self.button_color = (0, 255, 0)
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 48)
		# make button on the center
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center
		# повідомлення показати лише один раз
		self._prep_msg(msg)

	def _prep_msg(self, msg):
		"""перетворити текст на зображення та розмістити по центру кнопки"""
		self.image_msg = self.font.render(msg, True, self.text_color,
			self.button_color)
		self.image_msg_rect = self.image_msg.get_rect()
		self.image_msg_rect.center = self.rect.center

	def draw_button(self):
		# намалювати кнопку на екрані
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.image_msg, self.image_msg_rect)