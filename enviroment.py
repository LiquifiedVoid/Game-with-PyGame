import pygame
import random
from os import walk

class Enviroment():
    def __init__(self,display_surface):
        """Initialisiert die Enviroment Klasse und importiert die Bilder für die Umgebung und ordnet den Bildern eine zufällige Position zu.
        """
        self.surface = display_surface
        self.tile_size = 32
        self.ground_img = pygame.image.load("images/level/ground/tile058.png").convert_alpha()
        self.ground_img = pygame.transform.scale(self.ground_img,(self.tile_size,self.tile_size))
        self.all_decorations = []
        self.path = "images/level/decoration"
        
        #alle decorations
        for _,_,img_files in walk(self.path):
            for img in img_files:
                full_path = self.path + "/" + img    
                deco_surface = pygame.image.load(full_path).convert_alpha()
                deco_surface = pygame.transform.scale(deco_surface,(self.tile_size,self.tile_size))
                self.all_decorations.append(deco_surface)
        
        #zufällige positionen 
        self.positions = []
        for i in range(10,40):
            x = random.randrange(0,self.surface.get_width(),self.tile_size)
            y = random.randrange(0,self.surface.get_height(),self.tile_size)
            self.positions.append((x,y))
        
        #positionen einem deko element zuordnen
        self.pos_deco_duo = {}
        for pos in self.positions:
            self.pos_deco_duo[pos] = random.choice(self.all_decorations)  
        
    def update(self):
        """Updated die Umgebung und zeichnet sie auf den display_surface.
        """
        for x in range(0,self.surface.get_width(),self.tile_size):
            for y in range(0,self.surface.get_height(),self.tile_size):
                pygame.Surface.blit(self.surface, self.ground_img,(x,y))
        
        for pos, img in self.pos_deco_duo.items():
            pygame.Surface.blit(self.surface, img, pos)
         
        
