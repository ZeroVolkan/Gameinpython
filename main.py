from init import *
import pygame as pg
import options
import base


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
TILE = base.Tile()

def main():
    while True:
        screen.fill(BLACK)
        clock.tick(options.FPS)

        TileSet = base.TileSet(pos=(0, 0), tile=(50, 50))
        TileSet.add_object(TILE, pos=(3, 2))
        TileSet.add_object(TILE, pos=(5, 2))
        TileSet.add_object(TILE, pos=(3, 3))
        TileSet.add_object(TILE, pos=(7, 2))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

        TileSet.render()
        pg.display.flip()


if __name__ == "__main__":
    main()


