import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """alien class for creating alien sprites by the dozen(later used in grouping aliens with Group()
    they can move with update() they can be blit() for rendering the image,
    and they know if they are out of the screen rectangle with check_edges"""
    def __init__(self,def_settings,screen):
        super(Alien,self).__init__()
        self.screen = screen
        self.def_settings = def_settings
        
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        self.x = float(self.rect.x)
        
        
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        
    def blitme(self):
        self.screen.blit(self.image,self.rect)
    def update(self):
        self.x += (self.def_settings.alien_speed_factor*self.def_settings.fleet_direction)
        self.rect.x = self.x
