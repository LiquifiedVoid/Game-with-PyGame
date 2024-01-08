import pygame
from settings import *
from player import Player
from enemy import Enemy
import random
from enviroment import Enviroment
import sys
import math
from level_up_interface import Interface_levelup

class Level:
    def __init__(self):
        """Initialisiert die Level Klasse. 
        """
        ##Game
        #Display
        self.display_surface = pygame.display.get_surface()

        #Spawnpunkte für Gegner und Timer
        self.timer = 0
        self.y_for_top_bottom = [-10,self.display_surface.get_height()+10]
        
        #Spritegruppen
        self.player_sprite = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()
        self.projectile_group = pygame.sprite.Group()
        self.setup()

        pygame.font.init()
        
    def get_font(self,size):
        """Gibt eine Schriftart zurück mit gegebener 
        """
        font = pygame.font.Font("fonts/joystix monospace.otf", size)
        return font
    
    def spawn_enemys(self,dt):
        """Spawnt Gegner und updated den Timer.
        """
        self.spawn_positions = [(random.randint(0,self.display_surface.get_width()),random.choice(self.y_for_top_bottom))]
        self.timer -= dt
        if self.timer <= 0:
            self.enemy = Enemy(random.choice(self.spawn_positions), self.enemy_sprites, self.player, self.display_surface)
            self.timer = 1.5
        
    def setup(self):
        """Initialisiert die Umgebung und den Spieler.
        """
        self.env = Enviroment(self.display_surface)
        self.player = Player((self.display_surface.get_width()/2,self.display_surface.get_height()/2), self.player_sprite, self.projectile_group)
        self.level_up_interface = Interface_levelup(self.display_surface)
        
    def run_game(self,dt):
        """Updated die Umgebung, den Spieler, die Gegner und die Projektile.
        """
        self.env.update()
        self.spawn_enemys(dt)
        self.player_sprite.draw(self.display_surface)
        self.player_sprite.update(dt,self.display_surface)
        self.enemy_sprites.draw(self.display_surface)
        self.enemy_sprites.update(dt)
        self.projectile_group.draw(self.display_surface)
        self.projectile_group.update(dt,self.enemy,self.enemy_sprites,self.display_surface)

    def run_startscreen(self, dt):
        """Zeigt den Startscreen an und gibt zurück ob das Spiel gestartet werden soll."""
        center_x = self.display_surface.get_width()/2
        center_y = self.display_surface.get_height()/2
        mouse_pos = pygame.mouse.get_pos()
        
        self.env.update()
        self.player_sprite.draw(self.display_surface)
        self.enemy_sprites.draw(self.display_surface)
        self.projectile_group.draw(self.display_surface)
        self.player.xp.draw_xp_bar(self.display_surface)
        self.player.draw_healthbar(self.display_surface)
        self.player.wand.draw_cooldown(self.display_surface)
        #play button
        play_txt = self.get_font(70).render("Play",True,"black")
        play_rect = play_txt.get_rect()
        play_rect.center = (center_x,center_y-50)
        self.display_surface.blit(play_txt, play_rect)
        gray_box = pygame.image.load("images/level/rect.png")
        gray_box = pygame.transform.scale(gray_box, (play_rect.w, play_rect.h))
        gray_box.set_alpha(0)
        self.display_surface.blit(gray_box, play_rect.topleft)
        
        #quit button
        quit_txt = self.get_font(50).render("Quit", True, "black")
        quit_rect = quit_txt.get_rect()
        quit_rect.center = (center_x,center_y+50)
        self.display_surface.blit(quit_txt, quit_rect)
        gray_box2 = pygame.image.load("images/level/rect.png")
        gray_box2 = pygame.transform.scale(gray_box2, (quit_rect.w, quit_rect.h))
        gray_box2.set_alpha(0)
        self.display_surface.blit(gray_box2, quit_rect.topleft)

        #game name
        game_name = self.get_font(110).render("Game", True, "black")
        game_name_rect = game_name.get_rect()
        t = pygame.time.get_ticks()/3 
        sin  = math.sin(t/90) * 20
        game_name_rect.center = (center_x  ,center_y-250 + sin)
        self.display_surface.blit(game_name,game_name_rect)
        

        
        #check clicked
        for event in pygame.event.get():
            #quit
            if quit_rect.collidepoint(mouse_pos[0],mouse_pos[1])and event.type == pygame.MOUSEBUTTONUP:
                pygame.quit()
                sys.exit()
            #run game
            if play_rect.collidepoint(mouse_pos[0],mouse_pos[1])and event.type == pygame.MOUSEBUTTONUP:
                return True
    
    def run_level_up_interface(self,dt):
        self.level_up_interface.draw(dt)
        self.level_up_interface.update(dt)
        
