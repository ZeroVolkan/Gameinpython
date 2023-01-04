import sys
import engine

import pygame as pg


def main():

    space = engine.space.Space(pos=(0, 0))
    body1 = engine.node.Body(pos=(0, 0), wight=10, height=10)
    body2 = engine.node.Body(pos=(20, 20), wight=10, height=10)
    space.add_nodes([body1, body2])
    while True:
        engine.screen.fill(engine.options.BLACK)
        engine.clock.tick(engine.options.FPS)
        body1.render()
        body2.render()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        pg.display.flip()


if __name__ == "__main__":
    main()


