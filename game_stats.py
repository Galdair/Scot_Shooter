class GameStats():
    """game stats class for storing various statsitics 
    concerning the flow of the game,like high score
    ,normal score,and ships reaming and level which the player is currently on 
    TODO the high score hould be saved in a text file"""
    def __init__(self,def_settings):
        self.def_settings = def_settings
        self.reset_stats()
        self.score = 0
        self.game_active = False
        self.high_score = 0
    def reset_stats(self):
        self.ships_left = self.def_settings.ship_limit
        self.level = 1
