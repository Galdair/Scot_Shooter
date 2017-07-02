class Settings():
    def __init__(self):
        """initilaize A scotish setting!"""
        self.screen_width = 1280
        self.screen_height = 760
        self.bgcolor = (255,255,255)
        self.fleet_drop_speed = 10
        self.ship_limit = 3
        self.powerful_weapon_limiter = True
        self.speedup_scale = 1.2
        
        self.initialize_dynamic_settings()
    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 10
        self.alien_speed_factor = 1
        self.fleet_direction = 1
        self.alien_points = 50
    def increase_speed(self):
        self.ship_speed_factor  *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.fleet_direction *= self.speedup_scale
        self.alien_points = int(self.alien_points*self.speedup_scale)
