import sys
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,screen,ship):
        super(Bullet,self).__init__()
        self.ball_image = pygame.image.load('images/tennis_ball15.bmp')
        self.rect = self.ball_image.get_rect()
        self.ball_speed_factor = 25
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.centery = float(self.rect.y)
        
    def update(self):
        self.centery   -= self.ball_speed_factor
        self.rect.y =  self.centery
    def blitbullet(self,screen):
        screen.blit(self.ball_image,self.rect)
        
       
