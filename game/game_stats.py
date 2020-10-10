class GameStats():
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()

    def reset_stats(self):
        """Initializes statistical data that may change during the game"""
        self.ships_left = self.ai_settings.ship_limit