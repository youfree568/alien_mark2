class Settings:
	"""game settings"""
	def __init__(self):
		self.screen_width = 2000
		self.screen_height = 400
		self.bg_color = (230, 230, 230)
		self.ship_speed = 2
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullet_speed = 1
		self.bullet_allowed = 3
		self.alien_speed = 1.0
		self.fleet_drop_speed = 10
		self.fleet_direction = 1