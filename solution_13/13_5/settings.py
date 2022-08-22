class Settings:
	"""налаштування нашої програми"""
	def __init__(self):
		# розміри екрану
		self.screen_width = 800
		self.screen_height = 600
		# фон тла
		self.bg_color = (230, 230, 230)
		# bullet settings
		self.bullet_width = 15
		self.bullet_height = 30
		self.bullet_color = (60, 60, 60)
		self.bullet_speed = 0.5
		self.mario_speed = 0.1
		self.fleet_drop_speed = 30
		self.fleet_direction = 1
		self.ship_limit = 1