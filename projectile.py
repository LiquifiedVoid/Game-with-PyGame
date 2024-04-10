import pygame
from hilfe import *
import settings

class Projectile(pygame.sprite.Sprite):
    def __init__(self, player_pos, type, mouse_pos, speed):
        """Initialisiert die Projectile Klasse.
        """
        super().__init__()
        self.import_assets()
        self.image = pygame.Surface((10,50))
        self.frame_index = 0
        self.type = type
        self.mouse_pos = mouse_pos
        
        self.image = self.animations[self.type][self.frame_index]
        self.rect = self.image.get_rect(center=(player_pos))
        self.vector = pygame.Vector2(self.rect.center) 
        self.speed = speed
        
        self.hit_animate_help = 0
        
        self.hit_sound = pygame.mixer.Sound("music/hit.mp3")
        self.hit_sound.set_volume(0.1)
        self.play_sound = False
        self.played = False
        
    def import_assets(self):
        """Importiert die Bilder für die Projektile.
        """
        self.animations = {'fire': [], 'fire_hit' : []
			                }

        for animation in self.animations.keys():
            
            full_path = "images/wands/" + animation
            self.animations[animation] = import_folder(full_path,(32,32))    
    
    def move(self, dt):
        """Bewegt das Projektil in Richtung des Mauszeigers zum Zeitpunkt des schießens und löscht es, wenn es den Bildschirm verlässt.
        """
        if "hit" not in self.type:
            self.mouse_vector = pygame.Vector2(self.mouse_pos)
            self.movement = self.mouse_vector - self.vector
            self.movement.scale_to_length(self.speed)
                
            self.rect.x += self.movement.x * dt
            self.rect.y += self.movement.y * dt
                
            if self.rect.x > settings.SCREEN_WIDTH or self.rect.x < -10 or self.rect.y > settings.SCREEN_HEIGHT or self.rect.y < -10:
                self.kill()
          
    def check_hit(self,enemy,enemy_sprites):
        """Überprüft, ob das Projektil einen Gegner getroffen hat und lässt gegner HP fallen.
        """
        for enemy in enemy_sprites:
            if self.rect.colliderect(enemy.rect):
                enemy.status ="gameover"
                
                if "_" not in self.type:
                    self.type = self.type + "_hit" 
                enemy.drop_health()
               
        
    def animate(self,dt):
        """Animiert das Projektil. Wenn es ein Gegner getroffen hat, wird es nach der Hit-Animation gelöscht.
        """
        if "hit" not in self.type:
            self.frame_index += 4 * dt
            if self.frame_index >= len(self.animations[self.type]):
                self.frame_index = 0
            self.image = self.animations[self.type][int(self.frame_index)]
        elif "hit" in self.type:
            self.play_sound = True
            if self.frame_index >= len(self.animations[self.type]):
                self.frame_index = 0
                self.hit_animate_help +=1
                if self.hit_animate_help >= 2:
                    self.kill()
            self.image = self.animations[self.type][int(self.frame_index)]
            self.frame_index += 4 * dt
            
    def update(self,dt,enemy,enemy_sprites,surface):
        """Updated die Klasse Projectile.
        """
        self.move(dt)
        self.check_hit(enemy,enemy_sprites)
        self.animate(dt)
        if self.play_sound:
            if self.played == False:
                self.hit_sound.play()
                self.play_sound = False
                self.played = True
        
