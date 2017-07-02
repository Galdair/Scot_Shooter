import pygame
import sys
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard
def run_game():
    pygame.init()
    def_settings = Settings()
   
    screen = pygame.display.set_mode((def_settings.screen_width,def_settings.screen_height))
    pygame.display.set_caption("Scotish Invasion")
    ship = Ship(def_settings,screen)
    alien = Alien(def_settings,screen)
    bullets = Group()
    aliens = Group()
    
    stats = GameStats(def_settings)
    play_button = Button(def_settings,screen,"play")
    gf.create_fleet(def_settings,screen,ship,aliens)
    sb = ScoreBoard(def_settings,screen,stats)
    while True:
        
        gf.check_events(ship,bullets,screen,stats,play_button,aliens,def_settings)
        if stats.game_active:
            ship.update()
            gf.update_bullets(def_settings,screen,ship,aliens,bullets,stats,sb)
            gf.update_aliens(def_settings,stats,screen,ship,aliens,bullets)
        gf.update_screen(def_settings,screen,ship,bullets,aliens,play_button,stats,sb)
        
        pygame.display.flip()
      
run_game()
    
