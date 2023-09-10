import pygame as pg
from copy import deepcopy
from random import randint
from settings import *

class Level:
    def __init__(self , img_path : str , width : int, height : int, bitmap : list , treasure_spawn_pos : list, cam_x : int , cam_y : int) -> None:
        self.sprite = pg.image.load(img_path)
        self.width = width
        self.height = height
        self.bitmap = bitmap
        self.treasure_spawn_pos = treasure_spawn_pos
        self.image = pg.transform.scale2x(self.sprite)
        self.treasures = list()
        self.cam_x = cam_x
        self.cam_y = cam_y
        self.last_animation_time = 0
        self.animation_delay = 200
        self.player_x = 13
        self.player_y = 10

        
    def make_treasure_spawn(self, number_treasure : int):
        treasure_spawn_copy = deepcopy(self.treasure_spawn_pos)
        for _ in range(number_treasure):
            pos = randint(0 , len(treasure_spawn_copy))
            self.treasures.append(treasure_spawn_copy[pos])
            treasure_spawn_copy.pop(pos)

    def draw_map(self , WINDOW : pg.display):
        mask_surface = pg.Surface((500, 500), pg.SRCALPHA)
        mask_surface.fill((0 , 0 , 0 , 255))
        mask_radius = 48
        mask_center = (176 , 176)
        pg.draw.circle(mask_surface , (0 , 0, 0 , 0) , mask_center , mask_radius)


        WINDOW.blit(self.image , (0 , 0) , (self.cam_x, self.cam_y, WIN_HEIGHT ,WIN_WIDTH))
        WINDOW.blit(mask_surface , (0 , 0))

    def update_map(self):
        # Calculating the player position (in terms of index)
        player_left = self.cam_x // 32 + (WIN_WIDTH) // 32
        player_top = self.cam_y // 32 + (WIN_HEIGHT) // 32

        keys = pg.key.get_pressed()

        self.current_time = pg.time.get_ticks()
        if ((self.current_time - self.last_animation_time) < self.animation_delay):
            return
        
        if keys[pg.K_LEFT]:
            if (self.bitmap[self.player_y][self.player_x - 1] == 1):
                self.cam_x -= 32
                self.player_x -= 1
                print (self.player_x , self.player_y)
                self.last_animation_time = self.current_time
                return
            
        elif keys[pg.K_RIGHT]:
            if (self.bitmap[self.player_y][self.player_x + 1] == 1):
                self.cam_x += 32
                self.player_x += 1
                print (self.player_x , self.player_y)
                self.last_animation_time = self.current_time
                return
            
        elif keys[pg.K_UP]:
            if (self.bitmap[self.player_y - 1][self.player_x] == 1):
                self.cam_y -= 32
                self.player_y-= 1
                print (self.player_x , self.player_y)
                self.last_animation_time = self.current_time
                return

        elif keys[pg.K_DOWN]:
            if (self.bitmap[self.player_y + 1][self.player_x] == 1):
                self.cam_y += 32
                self.player_y += 1
                print (self.player_x , self.player_y)
                self.last_animation_time = self.current_time
                return
