import pygame
from projectile import Projectile


class Wand(): #Wand = Zauberstab
    def __init__(self, player_pos, group):
        """Initialisiert die Wand Klasse.
        """
        self.player_pos = player_pos
        self.base_cooldown = 120 #in frames (60 Frames = 1 Sekunde)
        self.current_cooldown = 0
        self.type = 'fire'
        self.group = group
        
    def draw_cooldown(self,screen):
        """Zeichnet den Cooldown des Wands auf den Screen.
        """
        self.cooldown_percentage = self.current_cooldown / self.base_cooldown
        pygame.draw.rect(screen,"royalblue4",(self.player_pos.x,self.player_pos.y+40, 30 * self.cooldown_percentage,8),
                         border_bottom_right_radius=15,border_top_right_radius=15)
        pygame.draw.rect(screen,"royalblue4",(self.player_pos.x-30*self.cooldown_percentage+1,self.player_pos.y+40, 30*self.cooldown_percentage,8),
                         border_bottom_left_radius=15,border_top_left_radius=15)
        
    def use(self,mouse_pos):
        """Fügt dem Spieler eine neue Projektile Instanz hinzu, aber nur wenn der Cooldown abgelaufen ist.
        """
        if self.current_cooldown == 0:
            self.mouse_pos = mouse_pos
            self.current_cooldown = self.base_cooldown
            self.group.add(Projectile(self.player_pos, self.type, self.mouse_pos))

        