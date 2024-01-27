import pygame
import sys
from settings import *
from level import Level
import event_handler as e_h

class Main:
    def __init__(self):
        pygame.init()
        #events für alle Klassen verfügbar machen
        self.eh = e_h.EventHandler()
        #Display
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Game!")
        #Clock
        self.clock = pygame.time.Clock()
        #Level und Game
        self.level = Level(self.eh)
        self.running = True
        self.state = "startscreen"
        
          
        
        
    def run(self):
        """Main loop des Spiels. Updated den Start/Pause-Screen oder das Spiel und wechselt zwischen ihnen. 
        """
        while self.running:
            if self.state == "startscreen":
                for event in self.eh.get_events():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                dt = self.clock.tick(60) / 1000
                run_game = self.level.run_startscreen(dt)
                if run_game:
                    self.state = "game"
                

            if self.state == "game":
                for event in self.eh.get_events():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        self.state = "startscreen"

                    if self.level.player.xp.level_up_hilfe:
                        self.state = "level_up"
                        self.level.player.xp.level_up_hilfe = False

                dt = self.clock.tick(60) / 1000
                self.level.run_game(dt)
                if self.level.player.show_gameover:
                    self.state = "gameover"
                    self.level.player.show_gameover = False    
            
            if self.state == "gameover":
                for event in self.eh.get_events():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                dt = self.clock.tick(60) / 1000
                self.level.run_gameover_interface(dt)
                if self.level.gameover_interface.restart:
                    self.state = "game"
                    self.level.gameover_interface.restart = False
                elif self.level.gameover_interface.quit:
                    pygame.quit()
                    sys.exit()
                               
            if self.state == "level_up":
                self.level.level_up_interface.upgrade_ausgewaehlt = False
                for event in self.eh.get_events():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                dt = self.clock.tick(60) / 1000
                self.level.run_level_up_interface(dt)
                if self.level.level_up_interface.upgrade_ausgewaehlt:
                    self.state = "game"
                
            pygame.display.update()


if __name__ == '__main__':
    """Startet das Spiel."""
    main = Main()
    main.run()
