import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A Class to manage them bullets"""

    def __init__(self, ai_settings, screen, ship):
        """Create a bullet object"""
        super(Bullet,self).__init__()
        self.screen = screen

        #create a bullet rect at 0,0
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #store bullets position as decimal
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor


    def update(self):
        """Move bullet up the screen"""
        #update decimal value of the bullet
        self.y -= self.speed_factor

        #update y.rect
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw a bullet"""
        pygame.draw.rect(self.screen, self.color, self.rect)