import pygame
import sys
import math


class Interface_Gameover():
    def __init__(self, screen, e_h):
        """ Initialisiert das Interface für den Gameover-Screen."""
        self.display_surface = screen
        self.eh = e_h
        

    def get_font(self, size):
        """Gibt eine Schriftart zurück mit gegebener Schriftgröße.
        """
        font = pygame.font.Font("fonts/joystix monospace.otf", size)
        return font

    def draw(self):
        """Zeichnet das Interface auf den Bildschirm und gibt True zurück, wenn der Restart-Button gedrückt wurde. Wenn der Quit-Button gedrückt wurde, wird das Spiel beendet.
        """
        center_x = self.display_surface.get_width()/2
        center_y = self.display_surface.get_height()/2
        mouse_pos = pygame.mouse.get_pos()

        # restart button
        restart_txt = self.get_font(70).render("Restart", True, "black")
        restart_rect = restart_txt.get_rect()
        restart_rect.center = (center_x, center_y-50)
        self.display_surface.blit(restart_txt, restart_rect)
        gray_box = pygame.image.load("images/level/rect.png")
        gray_box = pygame.transform.scale(
            gray_box, (restart_rect.w, restart_rect.h))
        gray_box.set_alpha(0)
        self.display_surface.blit(gray_box, restart_rect.topleft)

        # quit button
        quit_txt = self.get_font(50).render("Quit", True, "black")
        quit_rect = quit_txt.get_rect()
        quit_rect.center = (center_x, center_y+50)
        self.display_surface.blit(quit_txt, quit_rect)
        gray_box2 = pygame.image.load("images/level/rect.png")
        gray_box2 = pygame.transform.scale(
            gray_box2, (quit_rect.w, quit_rect.h))
        gray_box2.set_alpha(0)
        self.display_surface.blit(gray_box2, quit_rect.topleft)

        # gameover text
        game_name = self.get_font(110).render("Gameover", True, "black")
        game_name_rect = game_name.get_rect()
        t = pygame.time.get_ticks()/3
        sin = math.sin(t/90) * 20
        game_name_rect.center = (center_x, center_y-250 + sin)
        self.display_surface.blit(game_name, game_name_rect)

        # check clicked
        for event in self.eh.get_events():
            # quit
            if quit_rect.collidepoint(mouse_pos[0], mouse_pos[1]) and event.type == pygame.MOUSEBUTTONUP:
                pygame.quit()
                sys.exit()
            # restart game
            if restart_rect.collidepoint(mouse_pos[0], mouse_pos[1]) and event.type == pygame.MOUSEBUTTONUP:
                return True
