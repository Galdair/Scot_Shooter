import pygame


class Ship():
    def __init__(self,def_settings,screen):
        self.screen = screen
        self.def_settings = def_settings
        self.image = pygame.image.load('images/scotsman.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False
        self.center = float(self.screen_rect.centerx)
    def blitme(self):
        self.screen.blit(self.image,self.rect)
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.def_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.def_settings.ship_speed_factor
        self.rect.centerx = self.center
    def center_ship(self):
        self.center = self.screen_rect.centerx
