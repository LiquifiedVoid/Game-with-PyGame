import pygame
import sys


class Gameover_Interface():
    def __init__(self,screen, e_h, player):
        self.screen = screen
        self.eh = e_h
        self.player = player
        
        
    def restart(self):
        """Startet das Spiel neu.
        """
        pass
    
    def quit(self):
        """Beendet das Spiel.
        """
        pass
    
    def draw(self):
        """Zeichnet das Interface.
        """
        pass
    
    def update(self,dt):
        """Updated das Interface.
        """
        pass