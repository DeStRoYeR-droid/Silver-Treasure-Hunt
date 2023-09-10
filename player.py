import math
import pygame as pg
import os
from settings import *
from time import sleep

class Player:
    DOWN_ANIMATION_SPRITES = [
        pg.image.load("./assets/player_sprites/down_facing.png"),
        pg.image.load("./assets/player_sprites/down_moving_1.png"),
        pg.image.load("./assets/player_sprites/down_moving_2.png")
    ]

    UP_ANIMATION_SPRITES = [
        pg.image.load("./assets/player_sprites/up_facing.png"),
        pg.image.load("./assets/player_sprites/up_moving_1.png"),
        pg.image.load("./assets/player_sprites/up_moving_2.png")
    ]

    RIGHT_ANIMATION_SPRITES = [
        pg.image.load("./assets/player_sprites/right_facing.png"),
        pg.image.load("./assets/player_sprites/right_moving_1.png"),
        pg.image.load("./assets/player_sprites/right_moving_2.png")
    ]

    LEFT_ANIMATION_SPRITES = [
        pg.image.load("./assets/player_sprites/left_facing.png"),
        pg.image.load("./assets/player_sprites/left_moving_1.png"),
        pg.image.load("./assets/player_sprites/left_moving_2.png")
    ]

    ANIMATION_DELAY = 150
    def __init__(self, px, py : int, dir : str, window : pg.display) -> None:
        """
        
        """
        self.x = px
        self.y = py
        self.dir = dir
        self.animation_sprites = {
            "l" : [pg.transform.scale2x(sprite) for sprite in self.LEFT_ANIMATION_SPRITES] , 
            "u" : [pg.transform.scale2x(sprite) for sprite in self.UP_ANIMATION_SPRITES] , 
            "r" : [pg.transform.scale2x(sprite) for sprite in self.RIGHT_ANIMATION_SPRITES] , 
            "d" : [pg.transform.scale2x(sprite) for sprite in self.DOWN_ANIMATION_SPRITES]
        }
        self.current_sprite_index = 0
        self.current_sprite = self.animation_sprites[self.dir][self.current_sprite_index]
        self.window = window
        self.animation_delay = self.ANIMATION_DELAY
        self.last_animation_time = 0
        self.moving = False

    def draw_player(self):
        self.window.blit(self.current_sprite , (self.y , self.x))

    def update_player(self):
        self.current_time = pg.time.get_ticks()

        if ((self.current_time - self.last_animation_time) > self.animation_delay):
            self.last_animation_time = self.current_time
            self.current_sprite_index = (self.current_sprite_index + 1) % len(self.animation_sprites[self.dir])
            self.current_sprite = self.animation_sprites[self.dir][self.current_sprite_index]

        if (not(self.moving)):
            self.current_sprite = self.animation_sprites[self.dir][0]

    def handle_input(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_LEFT]:
            self.dir = "l"
            self.moving = True

        elif keys[pg.K_RIGHT]:
            self.dir = "r"
            self.moving = True

        elif keys[pg.K_UP]:
            self.dir = "u"
            self.moving = True

        elif keys[pg.K_DOWN]:
            self.dir = "d"
            self.moving = True
        
        else:
            self.moving = False

        
        

    