class GameStats:
	"""check statistics in the game"""

	def __init__(self, ai):
		"""game initialization"""
		self.settings = ai.settings
		self.reset_stats()
		self.game_active = False
		

	def reset_stats(self):
		"""statistics initializatio which can change alonge the game"""
		self.ships_left = self.settings.ship_limit