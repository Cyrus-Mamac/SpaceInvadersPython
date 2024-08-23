import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button

import game_functions as gf 

def run_game():
    #initialize game
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #play button
    play_button = Button(ai_settings, screen, "Play")   

    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    #make ship
    ship = Ship(ai_settings, screen)

    #make group for bullet and aliens
    bullets = Group()
    aliens = Group()
    
    #create a fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #make an alien
    alien = Alien(ai_settings, screen)
    #main loop
    while True:
        #key events
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        
        if stats.game_active:
            ship.update()
            bullets.update()
               
            #remove bullets to reduce lag
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)  

            #update aliens
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
   
        #update's the screen
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()