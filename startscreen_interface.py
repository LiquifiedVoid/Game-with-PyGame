import pygame
import sys
import math


class Interface_Startscreen():
    def __init__(self, screen, e_h, player):
        self.display_surface = screen
        self.eh = e_h
        self.player = player
        
        # sound
        size = 70
       
        self.music_on = pygame.image.load("images/level/startscreen/music-on.png")
        self.music_off = pygame.image.load("images/level/startscreen/music-off.png")
        self.info = pygame.image.load("images/level/startscreen/info.png")

        
        self.music_on = pygame.transform.scale(self.music_on, (size,size))
        self.music_off = pygame.transform.scale(self.music_off, (size,size))
        self.info = pygame.transform.scale(self.info, (60,60))

        
        self.music_state = self.music_on
        self.show_info = False

    def get_font(self, size):
        """Gibt eine Schriftart zurück mit gegebener 
        """
        font = pygame.font.Font("fonts/joystix monospace.otf", size)
        return font

    def draw(self, dt):
        """Zeichnet das Interface.
        """
        center_x = self.display_surface.get_width()/2
        center_y = self.display_surface.get_height()/2
        mouse_pos = pygame.mouse.get_pos()
        
        # play button
        play_txt = self.get_font(70).render("Play", True, "black")
        play_rect = play_txt.get_rect()
        play_rect.center = (center_x, center_y-50)
        self.display_surface.blit(play_txt, play_rect)
        gray_box = pygame.image.load("images/level/rect.png")
        gray_box = pygame.transform.scale(gray_box, (play_rect.w, play_rect.h))
        gray_box.set_alpha(0)
        self.display_surface.blit(gray_box, play_rect.topleft)

        # quit button
        quit_txt = self.get_font(50).render("Quit", True, "black")
        quit_rect = quit_txt.get_rect()
        quit_rect.center = (center_x, center_y+50)
        self.display_surface.blit(quit_txt, quit_rect)
        gray_box2 = pygame.image.load("images/level/rect.png")
        gray_box2 = pygame.transform.scale(gray_box2, (quit_rect.w, quit_rect.h))
        gray_box2.set_alpha(0)
        self.display_surface.blit(gray_box2, quit_rect.topleft)

        # game name
        game_name = self.get_font(110).render("Slime Rancher", True, "black")
        game_name_rect = game_name.get_rect()
        t = pygame.time.get_ticks()/3
        sin = math.sin(t/90) * 20
        game_name_rect.center = (center_x, center_y-250 + sin)
        self.display_surface.blit(game_name, game_name_rect)
        
        # #sound buttons
        
        music_on_rect = self.music_on.get_rect()
        music_off_rect = self.music_off.get_rect()
        info_rect = self.info.get_rect()
        
        
        music_on_rect.center = (1880,1040)
        music_off_rect.center = (1880,1040)
        info_rect.center = (40,1040)
        
        
        
        self.display_surface.blit(self.music_state, music_on_rect)
        self.display_surface.blit(self.info, info_rect)
        
        # check clicked
        for event in self.eh.get_events():
            # quit
            if quit_rect.collidepoint(mouse_pos[0], mouse_pos[1]) and event.type == pygame.MOUSEBUTTONUP:
                pygame.quit()
                sys.exit()
            # run game
            if play_rect.collidepoint(mouse_pos[0], mouse_pos[1]) and event.type == pygame.MOUSEBUTTONUP:
                return True
            
            #sound
            if music_on_rect.collidepoint(mouse_pos[0], mouse_pos[1]) and event.type == pygame.MOUSEBUTTONUP and self.music_state == self.music_on:
                self.music_state = self.music_off
                pygame.mixer.music.set_volume(0)
                
            elif music_off_rect.collidepoint(mouse_pos[0], mouse_pos[1]) and event.type == pygame.MOUSEBUTTONUP and self.music_state == self.music_off:
                self.music_state = self.music_on
                pygame.mixer.music.set_volume(0.05)
                
            if info_rect.collidepoint(mouse_pos[0], mouse_pos[1]):
                self.show_info = True
            else:
                self.show_info = False
                
        if self.show_info:
            self.display_surface.blit(self.get_font(25).render("use wasd to move", True, "black"), (mouse_pos[0],mouse_pos[1]-100))
            self.display_surface.blit(self.get_font(25).render("use mouse to aim and shoot", True, "black"), (mouse_pos[0],mouse_pos[1]-75))
            self.display_surface.blit(self.get_font(25).render("press esc to pause", True, "black"), (mouse_pos[0],mouse_pos[1]-50))
            self.display_surface.blit(self.get_font(25).render("hit slimes to level up", True, "black"), (mouse_pos[0],mouse_pos[1]-25))