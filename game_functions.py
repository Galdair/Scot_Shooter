import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep
def check_aliens_bottom(def_settings,stats,screen,ship,aliens,bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom  >= screen_rect.bottom:
            ship_hit(def_settings,stats,screen,ship,aliens,bullets)
            break
def ship_hit(def_settings,stats,screen,ship,aliens,bullets):
    if stats.ships_left > 0:
        stats.ships_left -= 1
        aliens.empty()
        bullets.empty()
        
        create_fleet(def_settings,screen,ship,aliens)
        ship.center_ship()
        sleep(0.5)
        
    else:
       stats.game_active = False
       pygame.mouse.set_visible(True)
       stats.score = 0
def check_events(ship,bullets,screen,stats,play_button,aliens,def_settings,sb):
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            if event.key == pygame.K_LEFT:
                ship.moving_left = True
            if event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen,ship)
                bullets.add(new_bullet)
            if event.key == pygame.K_c:
               def_settings.powerful_weapon_limiter = False
            if event.key == pygame.K_v:
               def_settings.powerful_weapon_limiter = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            if event.key == pygame.K_LEFT:
                ship.moving_left = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(stats,play_button,mouse_x,mouse_y,def_settings,screen,ship,aliens,bullets,sb)
            
            
def check_play_button(stats,play_button,mouse_x,mouse_y,def_settings,screen,ship,aliens,bullets,sb):
    if play_button.rect.collidepoint(mouse_x,mouse_y) and not stats.game_active:
        stats.game_active = True
        stats.reset_stats()
        pygame.mouse.set_visible(False)
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        aliens.empty()
        bullets.empty()
        create_fleet(def_settings,screen,ship,aliens)
        ship.center_ship()
        def_settings.initialize_dynamic_settings()
    
def update_bullets(def_settings,screen,ship,aliens,bullets,stats,sb): 
       for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)           
       collisions = pygame.sprite.groupcollide(bullets,aliens,def_settings.powerful_weapon_limiter,True)     
       if collisions:
           stats.score += def_settings.alien_points
           sb.prep_score()
       check_high_score(stats,sb)
       if len(aliens) == 0:
           bullets.empty()
           stats.level += 1
           sb.prep_level()
           def_settings.increase_speed()
           create_fleet(def_settings,screen,ship,aliens)  
            
def update_screen(def_settings, screen, ship,bullets,aliens,play_button,stats,sb):
    screen.fill((255,255,255))
    bg_image = pygame.image.load('images/flag_bg.bmp')
    
    bg_image = pygame.transform.scale(bg_image, (def_settings.screen_width,def_settings.screen_height))
    screen.blit(bg_image,(0,0))
    for bullet in bullets.sprites():
        bullet.blitbullet(screen)
        bullet.update() 
    sb.show_score()
    ship.blitme()
    aliens.draw(screen)
    if not stats.game_active:
        play_button.draw_button()
    
        
def check_fleet_edges(def_settings,aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(def_settings,aliens)
            break
            
def change_fleet_direction(def_settings,aliens):
    for alien in aliens.sprites():
        alien.rect.y += def_settings.fleet_drop_speed
    def_settings.fleet_direction *= -1
    
def update_aliens(def_settings,stats,screen,ship,aliens,bullets):
    check_fleet_edges(def_settings,aliens)
    aliens.update()
    check_aliens_bottom(def_settings,stats,screen,ship,aliens,bullets)
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(def_settings,stats,screen,ship,aliens,bullets)
        print("Ship hit!!")

def get_number_rows(def_settings,ship_height,alien_height):
    available_space_y = (def_settings.screen_height - (3*alien_height) - ship_height)
    number_rows = int(available_space_y / (2*alien_height))
    return number_rows
    
def get_number_aliens_x(def_settings, alien_width):
    available_space_x = def_settings.screen_width - 2*alien_width
    number_aliens_x = int(available_space_x /(2*alien_width))
    return number_aliens_x
    
def create_alien(def_settings,screen,aliens,alien,alien_number,row_number):
        alien = Alien(def_settings,screen)
        alien_width = alien.rect.width
        alien.x = alien_width + 2* alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2*alien.rect.height * row_number
        aliens.add(alien) 
        
def create_fleet(def_settings,screen,ship,aliens):
    alien = Alien(def_settings,screen)
    number_aliens_x = get_number_aliens_x(def_settings,alien.rect.width)
    number_rows = get_number_rows(def_settings,ship.rect.height,alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(def_settings,screen,aliens,alien,alien_number,row_number)
def check_high_score(stats,sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
