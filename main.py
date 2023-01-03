import sys
import pygame as pg
from init import *
import options
import tile
import body


def main():

    body1 = body.Body(pos=(30, 30), wight=100, height=100, color=options.WHITE)
    body2 = body.Body(pos=(60, 60), wight=100, height=100, color=options.RED)
    collision = body.Collision()
    print(collision.body(body1, body2))
    print(collision.body(body2, body1))
    while True:
        screen.fill(options.BLACK)
        clock.tick(options.FPS)

        body1.render()
        body2.render()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        pg.display.flip()


if __name__ == "__main__":
    main()


