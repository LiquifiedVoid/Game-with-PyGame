import pygame

class Player_xp():
    def __init__(self):
        """Initialisiert die Klasse Player_xp.
        """
        self.level = 0
        self.current_xp = 0
        self.xp_for_next_level = 10
        self.length = 600
        self.height = 15

        pygame.font.init()
        self.font = pygame.font.Font("fonts/joystix monospace.otf",12)
        
        self.level_up_hilfe = False
        
    def draw_xp_bar(self,screen):
        """Zeichnet die XP Bar auf den Screen und zeigt das aktuelle Level an.
        """
        x = screen.get_width()/2 - self.length/2
        y = 20
        self.current_xp_percentage = self.current_xp/self.xp_for_next_level
        pygame.draw.rect(screen, "grey",(x,y,self.length,self.height),border_radius=20)
        pygame.draw.rect(screen, (79, 128, 37),(x,y,self.length*self.current_xp_percentage,self.height),border_radius=20)

        text = self.font.render("Level " + str(self.level),True, "black")
        screen.blit(text,(x+10,y))
        
    def add_xp(self):
        """Fügt dem Spieler XP hinzu und levelt ihn hoch, wenn er genug XP hat.
        """
        if self.current_xp < self.xp_for_next_level:
            self.current_xp+=1
            if self.current_xp >= self.xp_for_next_level:
                self.level_up()
                
        
    def level_up(self):
        """Levelt den Spieler hoch und setzt die XP auf 0.
        """
        self.current_xp = 0
        self.xp_for_next_level += 10
        self.level += 1
        self.level_up_hilfe = True
        
    
    def update(self,screen):
        """Updated die Klasse Player_xp.
        """
        self.draw_xp_bar(screen)
    
