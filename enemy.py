import pygame
from settings import *
from hilfe import *

import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, group, player,surface):
        """Initialisiert die Enemy Klasse. 
        """
        super().__init__(group)
        
        self.import_assets()
        self.status = 'right'
        self.frame_index = random.randint(0,3)
        self.hit_animate_help = 0
        
        #player infos
        self.player = player
        self.player_pos = player.pos
        
        #general
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center= pos)
        self.surface = surface

        self.drop_hp_help = False

        #movement
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 100
    
    def import_assets(self):
        """Importiert die Animationen der Klasse.
        """
        self.animations = {'left': [],'right': [], 'gameover' :[],
			                }

        for animation in self.animations.keys():
            
            full_path = "images/enemy/" + animation
            self.animations[animation] = import_folder(full_path,(32,32))
        
    def animate(self,dt):
        """Animiert die Klasse und löst die gameover Animation aus, wenn die Klasse stirbt und lässt sie dann verschwinden und Leben fallen.
        """
        if self.status != "gameover":
            self.frame_index += 4 * dt
            if self.frame_index >= len(self.animations[self.status]):
                self.frame_index = 0
            self.image = self.animations[self.status][int(self.frame_index)]
        elif self.status == "gameover":
            self.frame_index += 4 * dt
            if self.hit_animate_help == 0:
                if self.frame_index != 0:
                    self.frame_index = 0
                    self.hit_animate_help +=1
            if self.frame_index >= len(self.animations[self.status]):
                self.drop_health()
                self.player.xp.add_xp()
                self.kill()
            else:
                self.image = self.animations[self.status][int(self.frame_index)]
            
    
    def move_to_player(self, dt):
        """Bewegt die Klasse zum Spieler durch die Berechnung eines Vektors und der Skalierung auf die Geschwindigkeit.
        """
        if self.status !="gameover":
            self.player_vector = self.player_pos
            self.enemy_vector = self.pos
            self.movement = self.player_vector - self.enemy_vector
            self.movement.scale_to_length(self.speed)
                
            self.pos.x += self.movement.x * dt 
            self.rect.centerx = self.pos.x + 1

            self.pos.y += self.movement.y * dt 
            self.rect.centery = self.pos.y + 1
                
            if self.movement.x < 0:
                self.status = "left"
            else:
                self.status ="right"
        else:
            pass

    def check_collision(self):
        """Überprüft ob die Klasse mit dem Spieler kollidiert und zieht ihm dann ein Leben ab (oder tötet den Spieler) und tötet sich selbst.
        """
        if self.rect.colliderect(self.player.rect):
            self.player.current_health_points -= 1
            if self.player.current_health_points <= 0:
                self.player.status = "gameover"
            self.kill()

    def drop_health(self):
        """Lässt die Klasse mit einer gewissen Wahrscheinlichkeit ein Leben fallen, wenn der Spieler nicht volle Leben hat.
        """
        if random.randint(0,600) == 1: #ca. 5% chance
                if self.player.max_health_points != self.player.current_health_points and not self.drop_hp_help:
                    self.player.current_health_points += 1
                    self.drop_hp_help = True
             
    def update(self, dt):
        """Updated die Klasse.
        """
        self.move_to_player(dt)
        self.check_collision()
        self.animate(dt)
        
        
        
