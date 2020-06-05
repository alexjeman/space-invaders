import pygame


class Settings:
    def __init__(self):
        # Screen settings
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = (0, 0, 0)
        self.bg = "images/background.png"
        self.ship_speed = 10
        # Bullet settings
        self.bullet_speed = 10
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (165, 0, 255)
        self.bullets_allowed = 3
        # Alien Settings
        self.alien_speed = 2.0
        self.fleet_drop_speed = 50
        self.fleet_direction = 1
