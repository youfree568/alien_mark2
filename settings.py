class Settings:
	"""game settings"""
	def __init__(self):
		"""initialization constant settings"""
		# screen settings
		self.screen_width = 2000
		self.screen_height = 400
		self.bg_color = (230, 230, 230)
		
		# ship settings
		self.ship_limit = 3
		
		# bullet settings
		self.bullet_width = 4
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullet_allowed = 3
		
		# alien settings
		self.fleet_drop_speed = 10
		
		# якщо швидко гра має прискорюватись
		self.speedup_scale = 1.1
		self.initialization_dynamic_settings()


	def initialization_dynamic_settings(self):
		"""initialization of variable settings"""
		self.ship_speed = 1.5
		self.bullet_speed = 3.0
		self.alien_speed = 0.8
		# always start on the right
		self.fleet_direction = 1

	def increse_speed(self):
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale