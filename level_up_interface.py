import pygame
import random

class Interface_levelup():
    def __init__(self,screen,e_h, player):
        """Initialisiert die Klasse Interface_levelup. 
        """
        self.screen = screen
        self.font = pygame.font.Font("fonts/joystix monospace.otf", 55)
        self.font2 = pygame.font.Font("fonts/joystix monospace.otf", 35)
        self.text_level_up = self.font.render("Level Up!", True, "white")
        self.level_up_rect = self.text_level_up.get_rect()
        self.level_up_rect.center = (self.screen.get_width()/2,self.screen.get_height()/2-320)
        
        self.text_choose = self.font2.render("Choose an upgrade", True, "white")
        self.choose_rect = self.text_choose.get_rect()
        self.choose_rect.center = (self.screen.get_width()/2,self.screen.get_height()/2-220)
        
        #player
        self.player = player
        
        self.upgrade_list = ["health","damage","speed","cooldown","projectile_speed"]
        
        self.center_x = self.screen.get_width()/2
        self.center_y = self.screen.get_height()/2
        
        #events
        self.eh = e_h
        
        #auswahlboxen
        self.box_width = 240
        self.box_height = 360
        self.box_1 = pygame.Rect(self.center_x-300,self.center_y-100,self.box_width,self.box_height)
        self.box_1.center = (self.center_x-320,self.center_y)
        self.box_2 = pygame.Rect(self.center_x-300,self.center_y-100,self.box_width,self.box_height)
        self.box_2.center = (self.center_x,self.center_y)
        self.box_3 = pygame.Rect(self.center_x-300,self.center_y-100,self.box_width,self.box_height)
        self.box_3.center = (self.center_x+320,self.center_y)
        self.upgrade_ausgewaehlt = False
        
        #farben initialisieren
        self.color_1 = "white"
        self.color_2 = "white"
        self.color_3 = "white"
        
        self.current_upgrades = []
        self.randomized = False
        
    def get_font(self,size):
        """Gibt eine Schriftart zurück mit gegebener 
        """
        font = pygame.font.Font("fonts/joystix monospace.otf", size)
        return font
       
    def draw(self, dt):
        """Zeichnet die Level Up Oberfläche auf den Screen.
        """
        if not self.randomized:
            self.randomize_upgrades()
            self.randomized = True
        self.screen.blit(self.text_level_up,self.level_up_rect)
        self.screen.blit(self.text_choose,self.choose_rect)
        pygame.draw.rect(self.screen, self.color_1, self.box_1, border_radius=25)
        pygame.draw.rect(self.screen, self.color_2, self.box_2, border_radius=25)
        pygame.draw.rect(self.screen, self.color_3, self.box_3, border_radius=25)
        self.screen.blit(self.get_font(30).render(self.current_upgrades[0], True, "black"),(self.box_1.x+20,self.box_1.y+20))
        self.screen.blit(self.get_font(30).render(self.current_upgrades[1], True, "black"),(self.box_2.x+20,self.box_2.y+20))#
        self.screen.blit(self.get_font(30).render(self.current_upgrades[2], True, "black"),(self.box_3.x+20,self.box_3.y+20))
        
    def update(self, dt):
        """ Updated die Level Up Oberfläche, indem es schaut welches Upgrade der Spieler wählt.
        """
        mouse_pos = pygame.mouse.get_pos()
        
        event_list = self.eh.get_events()
        
        #click events
        for event in event_list:
            #box 1
            if self.box_1.collidepoint(mouse_pos[0],mouse_pos[1])and event.type == pygame.MOUSEBUTTONUP:
                self.choose_upgrade(0)
                self.randomized = False
                self.upgrade_ausgewaehlt = True
            #box 2
            if self.box_2.collidepoint(mouse_pos[0],mouse_pos[1])and event.type == pygame.MOUSEBUTTONUP:
                self.choose_upgrade(1)
                self.randomized = False
                self.upgrade_ausgewaehlt = True            
            #box 3
            if self.box_3.collidepoint(mouse_pos[0],mouse_pos[1])and event.type == pygame.MOUSEBUTTONUP:
                self.choose_upgrade(2)
                self.randomized = False
                self.upgrade_ausgewaehlt = True

            #hover events
            #box 1
            if self.box_1.collidepoint(mouse_pos[0],mouse_pos[1]):
                #pygame.draw.rect(self.screen, "grey", self.box_1, border_radius=25)
                self.color_1 = "grey"
            else:
                self.color_1 = "white"
            #box 2
            if self.box_2.collidepoint(mouse_pos[0],mouse_pos[1]):
                #pygame.draw.rect(self.screen, "grey", self.box_2, border_radius=25)
                self.color_2 = "grey"
            else:
                self.color_2 = "white"
            #box 3
            if self.box_3.collidepoint(mouse_pos[0],mouse_pos[1]):
                #pygame.draw.rect(self.screen, "grey", self.box_3, border_radius=25)
                self.color_3 = "grey"
            else:
                self.color_3 = "white"
        
        
    def randomize_upgrades(self):
        """Wählt zufällig 3 Upgrades aus der Liste aus und speichert sie in self.current_upgrades.
        """
        self.current_upgrades = []
        for i in range(3):
            self.current_upgrades.append(random.choice(self.upgrade_list))
    
    def choose_upgrade(self,box):
        if self.current_upgrades[box] == "health":
            self.player.max_health_points += 1
            self.player.current_health_points += 1
        
        if self.current_upgrades[box] == "damage":
            print("damage")
        
        if self.current_upgrades[box] == "speed":
            print("speed")
        
        if self.current_upgrades[box] == "cooldown":
            print("cooldown")
        
        if self.current_upgrades[box] == "projectile_speed":
            print("projectile_speed")
        
        
        