import pygame
import random

class Interface_levelup():
    def __init__(self,screen):
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
        
        
        self.upgrade_list = ["health","damage","speed","attack_speed","projectile_speed","projectile_size"]
        
        self.center_x = self.screen.get_width()/2
        self.center_y = self.screen.get_height()/2
        
        #auswahlboxen
        self.box_width = 240
        self.box_height = 360
        self.box_1 = pygame.Rect(self.center_x-300,self.center_y-100,self.box_width,self.box_height)
        self.box_1.center = (self.center_x,self.center_y)
        self.box_2 = pygame.Rect(self.center_x-300,self.center_y-100,self.box_width,self.box_height)
        self.box_2.center = (self.center_x-320,self.center_y)
        self.box_3 = pygame.Rect(self.center_x-300,self.center_y-100,self.box_width,self.box_height)
        self.box_3.center = (self.center_x+320,self.center_y)
        print(self.box_1)
        self.upgrade_ausgewaehlt = False
        
    def get_font(self,size):
        """Gibt eine Schriftart zurück mit gegebener 
        """
        font = pygame.font.Font("fonts/joystix monospace.otf", size)
        return font
       
    def draw(self, dt):
        """Zeichnet die Level Up Oberfläche auf den Screen.
        """
        self.screen.blit(self.text_level_up,self.level_up_rect)
        self.screen.blit(self.text_choose,self.choose_rect)
        pygame.draw.rect(self.screen, "white", self.box_1, border_radius=25)
        pygame.draw.rect(self.screen, "white", self.box_2, border_radius=25)
        pygame.draw.rect(self.screen, "white", self.box_3, border_radius=25)
        pygame.draw.line(self.screen, "black", (840, 360),(840, 360),width=10)
        
    def update(self, dt):
        """ Updated die Level Up Oberfläche, indem es schaut welches Upgrade der Spieler wählt.
        """
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            #box 1
            if self.box_1.collidepoint(mouse_pos[0],mouse_pos[1])and event.type == pygame.MOUSEBUTTONUP:
                self.upgrade_ausgewaehlt = True
            #box 2
            if self.box_2.collidepoint(mouse_pos[0],mouse_pos[1])and event.type == pygame.MOUSEBUTTONUP:
                self.upgrade_ausgewaehlt = True            
            #box 3
            if self.box_3.collidepoint(mouse_pos[0],mouse_pos[1])and event.type == pygame.MOUSEBUTTONUP:
                self.upgrade_ausgewaehlt = True
    