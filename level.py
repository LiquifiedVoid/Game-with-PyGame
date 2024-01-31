import pygame
from settings import *
from player import Player
from enemy import Enemy
import random
from enviroment import Enviroment
from level_up_interface import Interface_levelup
from gameover_interface import Interface_Gameover
from startscreen_interface import Interface_Startscreen

class Level:
    def __init__(self, e_h):
        """Initialisiert die Level Klasse. 
        """
        # Game
        # Display
        self.display_surface = pygame.display.get_surface()

        # event handler
        self.eh = e_h

        # Spawnpunkte für Gegner und Timer
        self.timer = 0
        self.y_for_top_bottom = [-10, self.display_surface.get_height()+10]

        # Spritegruppen
        self.player_sprite = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()
        self.projectile_group = pygame.sprite.Group()
        self.setup()

        pygame.font.init()

    def get_font(self, size):
        """Gibt eine Schriftart zurück mit gegebener 
        """
        font = pygame.font.Font("fonts/joystix monospace.otf", size)
        return font

    def spawn_enemys(self, dt):
        """Spawnt Gegner und updated den Timer.
        """
        self.spawn_positions = [(random.randint(0, self.display_surface.get_width()), random.choice(self.y_for_top_bottom))]
        self.timer -= dt
        if self.timer <= 0:
            self.enemy = Enemy(random.choice(self.spawn_positions),self.enemy_sprites, self.player, self.display_surface)
            if self.player.xp.level >= 8:
                self.timer = 0.5
            else:
                self.timer = 2 - self.player.xp.level/5

    def setup(self):
        """Initialisiert die Umgebung und den Spieler.
        """
        self.env = Enviroment(self.display_surface)
        self.player = Player((self.display_surface.get_width(
        )/2, self.display_surface.get_height()/2), self.player_sprite, self.projectile_group)
        self.startscreen_interface = Interface_Startscreen(self.display_surface, self.eh, self.player)
        self.level_up_interface = Interface_levelup(self.display_surface, self.eh, self.player)
        self.gameover_interface = Interface_Gameover(self.display_surface, self.eh)
        
    def draw_crosshair(self):
        """Zeichnet das Fadenkreuz.
        """
        mouse_pos = pygame.mouse.get_pos()
        crosshair = pygame.image.load("images/player/crosshair.png")
        crosshair = pygame.transform.scale(crosshair, (32, 32))
        crosshair_rect = crosshair.get_rect(center=(mouse_pos[0], mouse_pos[1]))
        self.display_surface.blit(crosshair, crosshair_rect)
        
    def run_game(self, dt):
        """Updated die Umgebung, den Spieler, die Gegner und die Projektile.
        """
        self.env.update()
        self.spawn_enemys(dt)
        self.player_sprite.draw(self.display_surface)
        self.player_sprite.update(dt, self.display_surface)
        self.enemy_sprites.draw(self.display_surface)
        self.enemy_sprites.update(dt)
        self.projectile_group.draw(self.display_surface)
        self.projectile_group.update(dt, self.enemy, self.enemy_sprites, self.display_surface)
        pygame.event.set_grab(True)
        pygame.mouse.set_visible(False)
        self.draw_crosshair()
        
    def run_startscreen(self, dt):
        """Zeigt den Startscreen an und gibt zurück ob das Spiel gestartet werden soll."""
        

        self.env.update()
        self.player_sprite.draw(self.display_surface)
        self.enemy_sprites.draw(self.display_surface)
        self.projectile_group.draw(self.display_surface)
        self.player.xp.draw_xp_bar(self.display_surface)
        self.player.draw_healthbar(self.display_surface)
        self.player.wand.draw_cooldown(self.display_surface)
        play = self.startscreen_interface.draw()
        if play:
            return True
        pygame.mouse.set_visible(True)
        

    def run_level_up_interface(self, dt):
        """ Zeigt das Level Up Interface an und updated es. Der Rest des Spiels wird pausiert."""

        self.env.update()
        self.player_sprite.draw(self.display_surface)
        self.enemy_sprites.draw(self.display_surface)
        self.projectile_group.draw(self.display_surface)
        self.player.xp.draw_xp_bar(self.display_surface)
        self.player.draw_healthbar(self.display_surface)
        self.player.wand.draw_cooldown(self.display_surface)
        self.level_up_interface.draw()
        self.level_up_interface.update()
        pygame.mouse.set_visible(True)
        
    def run_gameover_interface(self, dt):
        """ Zeigt das Gameover Interface an und updated es. Der Rest des Spiels wird pausiert. Gibt zurück ob das Spiel neugestartet werden soll."""
        self.env.update()
        self.player_sprite.draw(self.display_surface)
        self.enemy_sprites.draw(self.display_surface)
        self.projectile_group.draw(self.display_surface)
        self.player.xp.draw_xp_bar(self.display_surface)
        self.player.draw_healthbar(self.display_surface)
        self.player.wand.draw_cooldown(self.display_surface)
        restart = self.gameover_interface.draw()
        if restart:
            return True
        pygame.mouse.set_visible(True)