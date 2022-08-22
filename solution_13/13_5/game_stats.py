class GameStats:
	def __init__(self, ai):
		"""stat initialization"""
		self.settings = ai.settings
		self.reset_stats()
		self.game_active = True

	def reset_stats(self):
		"""ініціалізація статистики що може змінюватись в продовж гри"""
		self.ships_left = self.settings.ship_limit