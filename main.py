import pygame
import sys
from settings import *
from level import Level
import event_handler as e_h


class Main:
    def __init__(self):
        """ Initialisiert das Spiel und die Level Klasse."""
        pygame.init()
        # events für alle Klassen verfügbar machen
        self.eh = e_h.EventHandler()
        # Display
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Game!")
        # Clock
        self.clock = pygame.time.Clock()
        # Level und Game
        self.level = Level(self.eh)  # Steurung des Spiels
        self.running = True
        self.state = "startscreen"
        self.volume_music = 0.05
        pygame.mixer.music.load("music/menu.mp3")
        pygame.mixer.music.set_volume(self.volume_music)
        pygame.mixer.music.play(-1)
        


    def run(self):
        """Main loop des Spiels. Updated den Start/Pause/Gameover/Levelup-Screen oder das Spiel und wechselt zwischen ihnen. 
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
                    if self.level.startscreen_interface.music_state == self.level.startscreen_interface.music_on:
                        pygame.mixer.music.load("music/phase1.mp3")
                        pygame.mixer.music.set_volume(0.05)
                        pygame.mixer.music.play(-1)
                    else:
                        pygame.mixer.music.load("music/phase1.mp3")
                        pygame.mixer.music.set_volume(0)
                        pygame.mixer.music.play(-1)

            if self.state == "game":
                for event in self.eh.get_events():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        self.state = "startscreen"
                        if self.level.startscreen_interface.music_state == self.level.startscreen_interface.music_on:
                            pygame.mixer.music.load("music/menu.mp3")
                            pygame.mixer.music.set_volume(0.05)
                            pygame.mixer.music.play(-1)
                        else:
                            pygame.mixer.music.load("music/menu.mp3")
                            pygame.mixer.music.set_volume(0)
                            pygame.mixer.music.play(-1)

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
                restart_game = self.level.run_gameover_interface(dt)
                if restart_game:
                    self.level = Level(self.eh)
                    self.state = "game"

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
