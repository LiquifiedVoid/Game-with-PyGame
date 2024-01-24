import pygame
import sys
from settings import *
from level import Level


class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Game!")
        self.clock = pygame.time.Clock()
        self.level = Level()
        self.running = True
        self.state = "startscreen"

    def run(self):
        """Main loop des Spiels. Updated den Start/Pause-Screen oder das Spiel und wechselt zwischen ihnen. 
        """
        while self.running:
            if self.state == "startscreen":
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                dt = self.clock.tick(60) / 1000
                run_game = self.level.run_startscreen(dt)
                if run_game:
                    self.state = "game"
                pygame.display.update()

            if self.state == "game":
                for event in pygame.event.get():
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
                pygame.display.update()

            if self.state == "level_up":
                self.level.level_up_interface.upgrade_ausgewaehlt = False
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                self.level.run_level_up_interface(dt)
                if self.level.level_up_interface.upgrade_ausgewaehlt:
                    self.state = "game"
                pygame.display.update()


if __name__ == '__main__':
    """Startet das Spiel."""
    main = Main()
    main.run()
