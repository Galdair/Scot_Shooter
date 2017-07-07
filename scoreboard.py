import pygame.font

class ScoreBoard():
    """scoreboard class for displaying score,high score,and level of the game
    it has functions for prepping each variable,
    turning the variable into a string and turning it into a picture and after that getting a screen for it
    and after thet blitting every image with show_score(self)
    the init takes care of the neceassy colors
     i use a different color in prep_high_score becouse of the flag is blue there,that is a blue vaule by the way"""
    def __init__(self,def_settings,screen,stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.def_settings = def_settings
        self.stats = stats
        
        self.text_color = (32,34,23)
        self.font = pygame.font.SysFont(None,48)
        
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
    def prep_score(self):
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str,True,self.text_color,self.def_settings.bgcolor)
        
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right -20
        self.score_rect.top = 20
        
    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        
        
    def prep_high_score(self):
        high_score_str = str(self.stats.high_score)
        self.high_score_image = self.font.render(high_score_str,True,self.text_color,(0,101,189))
        
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
    def prep_level(self):
        self.level_image = self.font.render(str(self.stats.level),True,self.text_color,self.def_settings.bgcolor)
        
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
