import pygame


class Settings:
    def __init__(self):
        # Screen settings
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = (0, 0, 0)
        self.bg = "images/background.png"

        # Bullet settings
        self.bullet_speed = 20
        self.bullet_width = 10
        self.bullet_height = 25
        self.bullet_color = (165, 0, 255)
        self.bullets_allowed = 6
        # Alien Settings
        self.alien_speed = 5.0
        self.fleet_drop_speed = 200
        self.fleet_direction = 1
        # Ship settings
        self.ship_speed = 10
        self.ship_limit = 3
