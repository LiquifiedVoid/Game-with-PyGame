import pygame

class EventHandler:
    def __init__(self):
        """Initialisiert die Klasse EventHandler.
        """
        self.events = pygame.event.get()
        
    
    def get_events(self):
        """Gibt die Events zurück.
        """
        self.events = pygame.event.get()
        return self.events
#pygame.event.get() nur einmal ausführen und an alle Klassen,Methoden etc. weitergeben die diese brauchen. 
#Bei mehreren parallel audfgerufenen pygame.event.get() kann es zu Problemen kommen, 
# da immer ein event nur in einem Aufruf von pygame.event.get() auftauchen kann und somit ein event verloren gehen kann.