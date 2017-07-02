class GameStats():
    
    def __init__(self,def_settings):
        self.def_settings = def_settings
        self.reset_stats()
        self.score = 0
        self.game_active = False
    def reset_stats(self):
        self.ships_left = self.def_settings.ship_limit
