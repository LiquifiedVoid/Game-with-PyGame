import pygame
import random


class Interface_levelup():
    def __init__(self, screen, e_h, player):
        """Initialisiert die Klasse Interface_levelup. 
        """
        self.screen = screen
        self.font = pygame.font.Font("fonts/joystix monospace.otf", 55)
        self.font2 = pygame.font.Font("fonts/joystix monospace.otf", 35)
        self.text_level_up = self.font.render("Level Up!", True, "white")
        self.level_up_rect = self.text_level_up.get_rect()
        self.level_up_rect.center = (
            self.screen.get_width()/2, self.screen.get_height()/2-320)

        self.text_choose = self.font2.render(
            "Choose an upgrade", True, "white")
        self.choose_rect = self.text_choose.get_rect()
        self.choose_rect.center = (
            self.screen.get_width()/2, self.screen.get_height()/2-220)

        # player
        self.player = player

        self.upgrade_list = ["health", "speed", "cooldown", "projectile_speed"]

        self.size_upgrade = 100
        self.health_image = pygame.transform.scale(pygame.image.load(
            "images/level/level_up_screen/health.png"), (self.size_upgrade, self.size_upgrade))
        self.speed_image = pygame.transform.scale(pygame.image.load(
            "images/level/level_up_screen/speed.png"), (self.size_upgrade, self.size_upgrade))
        self.cooldown_image = pygame.transform.scale(pygame.image.load(
            "images/level/level_up_screen/cooldown.png"), (self.size_upgrade, self.size_upgrade))
        self.projectile_speed_image = pygame.transform.scale(pygame.image.load(
            "images/level/level_up_screen/projectile_speed.png"), (self.size_upgrade, self.size_upgrade))

        self.center_x = self.screen.get_width()/2
        self.center_y = self.screen.get_height()/2

        # events
        self.eh = e_h

        # auswahlboxen
        self.box_width = 240
        self.box_height = 360
        self.box_1 = pygame.Rect(
            self.center_x-300, self.center_y-100, self.box_width, self.box_height)
        self.box_1.center = (self.center_x-320, self.center_y)
        self.box_2 = pygame.Rect(
            self.center_x-300, self.center_y-100, self.box_width, self.box_height)
        self.box_2.center = (self.center_x, self.center_y)
        self.box_3 = pygame.Rect(
            self.center_x-300, self.center_y-100, self.box_width, self.box_height)
        self.box_3.center = (self.center_x+320, self.center_y)
        self.upgrade_ausgewaehlt = False

        # hover
        self.hover_1 = False
        self.hover_2 = False
        self.hover_3 = False

        # farben initialisieren
        self.color_1 = "white"
        self.color_2 = "white"
        self.color_3 = "white"

        self.current_upgrades = []
        self.randomized = False

        # upgrade level
        self.health_level = 0
        self.speed_level = 0
        self.cooldown_level = 0
        self.projectile_speed_level = 0

    def get_font(self, size):
        """Gibt eine Schriftart zurück mit gegebener 
        """
        font = pygame.font.Font("fonts/joystix monospace.otf", size)
        return font

    def draw(self, dt):
        """Zeichnet die Level Up Oberfläche auf den Screen.
        """
        if not self.randomized:
            self.randomize_upgrades()
            self.randomized = True
        self.screen.blit(self.text_level_up, self.level_up_rect)
        self.screen.blit(self.text_choose, self.choose_rect)
        pygame.draw.rect(self.screen, self.color_1,
                         self.box_1, border_radius=25)
        pygame.draw.rect(self.screen, self.color_2,
                         self.box_2, border_radius=25)
        pygame.draw.rect(self.screen, self.color_3,
                         self.box_3, border_radius=25)
        # self.screen.blit(self.get_font(30).render(self.current_upgrades[0], True, "black"),(self.box_1.x+20,self.box_1.y+20))
        # self.screen.blit(self.get_font(30).render(self.current_upgrades[1], True, "black"),(self.box_2.x+20,self.box_2.y+20))#
        # self.screen.blit(self.get_font(30).render(self.current_upgrades[2], True, "black"),(self.box_3.x+20,self.box_3.y+20))

        for i in range(3):
            box = getattr(self, "box_"+str(i+1))

            if self.current_upgrades[i] == "health":
                self.screen.blit(
                    self.health_image, (box.center[0]-self.size_upgrade/2, box.center[1]-self.size_upgrade/2))
                self.screen.blit(self.get_font(30).render(
                    "Level: "+str(self.health_level), True, "black"), (box.x+20, box.y+20))

            if self.current_upgrades[i] == "speed":
                self.screen.blit(
                    self.speed_image, (box.center[0]-self.size_upgrade/2, box.center[1]-self.size_upgrade/2))
                self.screen.blit(self.get_font(30).render(
                    "Level: "+str(self.speed_level), True, "black"), (box.x+20, box.y+20))

            if self.current_upgrades[i] == "cooldown":
                self.screen.blit(
                    self.cooldown_image, (box.center[0]-self.size_upgrade/2, box.center[1]-self.size_upgrade/2))
                self.screen.blit(self.get_font(30).render(
                    "Level: "+str(self.cooldown_level), True, "black"), (box.x+20, box.y+20))

            if self.current_upgrades[i] == "projectile_speed":
                self.screen.blit(self.projectile_speed_image, (
                    box.center[0]-self.size_upgrade/2, box.center[1]-self.size_upgrade/2))
                self.screen.blit(self.get_font(30).render(
                    "Level: "+str(self.projectile_speed_level), True, "black"), (box.x+20, box.y+20))

        if self.hover_1:
            self.show_tooltip(self.current_upgrades[0], pygame.mouse.get_pos())
        if self.hover_2:
            self.show_tooltip(self.current_upgrades[1], pygame.mouse.get_pos())
        if self.hover_3:
            self.show_tooltip(self.current_upgrades[2], pygame.mouse.get_pos())

    def update(self, dt):
        """ Updated die Level Up Oberfläche, indem es schaut welches Upgrade der Spieler wählt.
        """
        mouse_pos = pygame.mouse.get_pos()

        event_list = self.eh.get_events()

        # click events
        for event in event_list:
            # box 1
            if self.box_1.collidepoint(mouse_pos[0], mouse_pos[1]) and event.type == pygame.MOUSEBUTTONUP:
                self.choose_upgrade(0)
                self.randomized = False
                self.upgrade_ausgewaehlt = True
            # box 2
            if self.box_2.collidepoint(mouse_pos[0], mouse_pos[1]) and event.type == pygame.MOUSEBUTTONUP:
                self.choose_upgrade(1)
                self.randomized = False
                self.upgrade_ausgewaehlt = True
            # box 3
            if self.box_3.collidepoint(mouse_pos[0], mouse_pos[1]) and event.type == pygame.MOUSEBUTTONUP:
                self.choose_upgrade(2)
                self.randomized = False
                self.upgrade_ausgewaehlt = True

            # hover events
            # box 1
            if self.box_1.collidepoint(mouse_pos[0], mouse_pos[1]):
                # pygame.draw.rect(self.screen, "grey", self.box_1, border_radius=25)
                self.color_1 = "grey"
                self.hover_1 = True
                # self.show_tooltip(self.current_upgrades[0],mouse_pos)
            else:
                self.color_1 = "white"
                self.hover_1 = False
            # box 2
            if self.box_2.collidepoint(mouse_pos[0], mouse_pos[1]):
                # pygame.draw.rect(self.screen, "grey", self.box_2, border_radius=25)
                self.color_2 = "grey"
                self.hover_2 = True
                # self.show_tooltip(self.current_upgrades[1],mouse_pos)
            else:
                self.color_2 = "white"
                self.hover_2 = False
            # box 3
            if self.box_3.collidepoint(mouse_pos[0], mouse_pos[1]):
                # pygame.draw.rect(self.screen, "grey", self.box_3, border_radius=25)
                self.color_3 = "grey"
                self.hover_3 = True
                # self.show_tooltip(self.current_upgrades[2],mouse_pos)
            else:
                self.color_3 = "white"
                self.hover_3 = False

    def show_tooltip(self, upgrade, mouse_pos):
        """Zeigt einen Tooltip für das jeweilige Upgrade an."""

        if upgrade == "health":
            self.draw_tooltip(
                "Health", "Increases your maximum health by 1", mouse_pos)
        if upgrade == "speed":
            self.draw_tooltip(
                "Speed", "Increases your movement speed by 20%", mouse_pos)
        if upgrade == "cooldown":
            self.draw_tooltip(
                "Cooldown", "Decreases your wand cooldown by 20%", mouse_pos)
        if upgrade == "projectile_speed":
            self.draw_tooltip(
                "Projectile Speed", "Increases your projectile speed by 20%", mouse_pos)

    def draw_tooltip(self, title, text, mouse_pos):
        """Zeichnet einen Tooltip mit dem gegebenen Titel und Text an der gegebenen Position."""
        self.screen.blit(self.get_font(25).render(
            title, True, "black"), (mouse_pos[0]+20, mouse_pos[1]+20))
        self.screen.blit(self.get_font(15).render(
            text, True, "black"), (mouse_pos[0]+20, mouse_pos[1]+50))

    def randomize_upgrades(self):
        """Wählt zufällig 3 Upgrades aus der Liste aus und speichert sie in self.current_upgrades.
        """
        self.current_upgrades = []
        for i in range(3):
            self.current_upgrades.append(random.choice(self.upgrade_list))

    def choose_upgrade(self, box):
        """ Wählt das Upgrade aus der Liste aus, das in der gegebenen Box ist."""

        if self.current_upgrades[box] == "health":
            self.player.max_health_points += 1
            self.player.current_health_points += 1
            self.health_level += 1

        if self.current_upgrades[box] == "speed":
            self.player.speed = self.player.speed * 1.2
            self.speed_level += 1

        if self.current_upgrades[box] == "cooldown":
            self.player.wand.base_cooldown = self.player.wand.base_cooldown * 0.8
            self.cooldown_level += 1

        if self.current_upgrades[box] == "projectile_speed":
            self.player.wand.projectile_speed = self.player.wand.projectile_speed * 1.2
            self.projectile_speed_level += 1
