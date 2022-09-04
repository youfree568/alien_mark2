class Settings:

	def __init__(self):
		"""initialization constant settings"""
		# screen settings
		self.screen_width = 600
		self.screen_height = 400
		self.bg_color = (200, 200, 200)
		
		# bullet settings
		self.bullet_width = 15
		self.bullet_height = 3
		self.bullet_color = (100, 10, 10)
		
		self.bullet_allowed = 5
		# target settings
		self.target_width = 10
		self.target_height = 100
		self.target_color = (100, 100, 100)
		self.missed_target = 5
		self.hit_target = 0
		
		self.speedup_scale = 1.3
		self.target_direction = 1
		self.initialization_dynamic_settings_easy()
		self.initialization_dynamic_settings_hard()

	def initialization_dynamic_settings_easy(self):
		self.ship_speed = 0.1
		self.bullet_speed = 0.9
		self.target_speed = 0.05

	def initialization_dynamic_settings_hard(self):
		self.ship_speed = 0.7
		self.bullet_speed = 2.2
		self.target_speed = 0.5

	def increase_speed(self):
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.target_speed *= self.speedup_scale