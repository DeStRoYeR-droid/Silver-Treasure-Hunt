import pygame as pg
import sys
import array
from levels import *
from settings import *
from player import Player

# Global variables
CUR_LEVEL = 0 # Indexing

# Initialising the module
pg.init()

BOARD = pg.display.set_mode((WIN_HEIGHT, WIN_WIDTH))
PLAYER = Player(WIN_WIDTH // 2 + 16, WIN_HEIGHT // 2  , "d" , BOARD)
CLOCK = pg.time.Clock()
CUR_LEVEL = LEVEL_1

# Main game loop
def main():
    RUN = True
    while RUN:
        CLOCK.tick(FPS)
        for event in pg.event.get():
            if (event.type == pg.QUIT):
                RUN = False
                break
            
            PLAYER.handle_input()

        BOARD.fill(BLACK)
        LEVEL_1.update_map()
        LEVEL_1.draw_map(BOARD)
        PLAYER.update_player()
        PLAYER.draw_player()
        
        pg.display.flip()


if __name__ == "__main__":
    main()
