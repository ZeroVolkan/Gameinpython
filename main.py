from init import *
import pygame as pg
import options
import base


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


def main():

    TileSet = base.TileSet((0, 0), (50, 50), wight=200, height=200)
    TileSet.add_object(base.Tile((1, 2)))

    while True:

        screen.fill(BLACK)
        clock.tick(options.FPS)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

        TileSet.render()


        pg.display.flip()


if __name__ == "__main__":
    main()


