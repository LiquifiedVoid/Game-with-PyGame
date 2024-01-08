import pygame
import random

class Interface_levelup():
    def __init__(self,screen):
        """Initialisiert die Klasse Interface_levelup.
        """
        self.screen = screen
        self.font = pygame.font.Font("fonts/joystix monospace.otf", 20)
        self.text_level_up = self.font.render("Level Up!", True, "white")
        self.level_up_rect = self.text_level_up.get_rect()
        self.level_up_rect.center = (self.screen.get_width()/2,self.screen.get_height()/2)
        
        self.upgrade_list = ["health","damage","speed","attack_speed","projectile_speed","projectile_size"]
        
        
    def draw(self, dt):
        self.screen.blit(self.text_level_up,self.level_up_rect)
        print("hier")
    def update(self, dt):
        pass