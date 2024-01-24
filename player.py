import pygame
from settings import *
from hilfe import *
from timer import Timer
from wand import Wand
from player_xp import Player_xp

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group, projectile_group):
        """Initialisiert die Player Klasse.
        """
        super().__init__(group)
        self.import_assets()
        self.status = 'down_idle'
        self.frame_index = 0
        self.animate_bool = True
        self.projectile_group = projectile_group

        #player stats
        self.speed = 150
        self.max_health_points = 3
        self.current_health_points = 3
        self.xp = Player_xp()
        
        #general
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center= pos)
        
        #movement
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        
        #font setup for +1 health
        self.font = pygame.font.Font("fonts/joystix monospace.otf", 20)
        self.text_dropped_health = self.font.render("+1 HP", True, "red")
        self.dropped_health_rect = self.text_dropped_health.get_rect()
        
        #wand
        self.wand = Wand(self.pos, projectile_group)
        
    def import_assets(self):
        """Importiert die Bilder für die Animationen des Spielers.
        """
        self.animations = {'up': [],'down': [],'left': [],'right': [], 'gameover' :[],
						   'right_idle':[],'left_idle':[],'up_idle':[],'down_idle':[],
			                }

        for animation in self.animations.keys():
            
            full_path = "images/player/" + animation
            self.animations[animation] = import_folder(full_path,(48,64))
        
    def animate(self,dt):
        """Animiert den Spieler.
        """
        if self.animate_bool:
            self.frame_index += 4 * dt
            if self.frame_index >= len(self.animations[self.status]) and self.status == "gameover":
                self.animate_bool = False
                
            else:
                if self.frame_index >= len(self.animations[self.status]):
                    self.frame_index = 0
                self.image = self.animations[self.status][int(self.frame_index)]
        
    def input(self):
        """Überprüft die Tastatureingaben und bewegt den Spieler. Es wird auch überprüft, ob der Spieler den Zauberstab benutzt.
        """
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w] and self.status != "gameover":
            self.direction.y = -1
            self.status = "up"
        elif keys[pygame.K_s]and self.status != "gameover":
            self.direction.y = 1
            self.status = "down"
        else:
            self.direction.y = 0
            
        if keys[pygame.K_a]and self.status != "gameover":
            self.direction.x = -1
            self.status = "left"
        elif keys[pygame.K_d]and self.status != "gameover":
            self.direction.x = 1 
            self.status = "right"
        else:
            self.direction.x = 0

        #wand
        if pygame.mouse.get_pressed()[0]:
            self.use_wand()
            
    def use_wand(self):
        """Benutzt den Zauberstab.
        """
        if self.status != "gameover":
            self.mouse_pos = pygame.mouse.get_pos()
            self.wand.use(self.mouse_pos)
            

    def check_idle(self):
        """Überprüft, ob der Spieler sich bewegt. Wenn nicht, wird er auf idle gesetzt.
        """
        if self.direction.magnitude() == 0 and self.status != "gameover":
            self.status = self.status.split("_")[0] + "_idle"
    
    def move(self,dt):
        """Bewegt den Spieler in die Richtung, in die er sich bewegen soll.
        """
        #gleiche bewegung auch für diagonal
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()
        
        #horizontale
        self.pos.x += self.direction.x * self.speed *dt
        self.rect.centerx = self.pos.x
        
        #vertikale
        self.pos.y += self.direction.y * self.speed *dt
        self.rect.centery = self.pos.y

    def check_gameover(self): #!!!!TODO: gameover screen
        if self.status == "gameover":
            pass

    def draw_healthbar(self,screen):
        """Zeichnet die Healthbar des Spielers auf den Screen.
        """
        x = self.rect.topleft[0]
        y = self.rect.topleft[1]
        
        if self.current_health_points >= 0:
            self.current_health_percentage = self.current_health_points / self.max_health_points
        pygame.draw.rect(screen, "grey", (x,y-15,50,10),border_radius=10)
        pygame.draw.rect(screen, "red", (x,y-15,50*self.current_health_percentage,10),border_radius=10)

    def get_pos(self):
        return self.pos
        
    def update(self, dt, screen):
        """Updated die Player Klasse und seinen Zauberstab.
        """
        self.input()
        self.check_idle()

        self.draw_healthbar(screen)
        self.xp.update(screen)
        if self.wand.current_cooldown > 0:
            self.wand.current_cooldown -= 1
        self.wand.draw_cooldown(screen)
        
        self.move(dt)
        self.animate(dt)
        
        
