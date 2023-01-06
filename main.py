import sys
import engine

import pygame as pg


def main():

    collision = engine.collision.Collision("collision")
    gravity = engine.effect.Gravity("gravity")
    stop_gravity = engine.effect.StopEffectIfSignal("stop_gravity", "gravity", "collision")

    space = engine.space.Space(pos=(0, 0), wight=1000, height=1000)
    space.add_effect(collision)

    body1 = engine.node.Body(pos=(0, 0), wight=100, height=100)
    body2 = engine.node.Body(pos=(0, 400), wight=100, height=100, color=engine.options.RED)

    space.add_nodes([body1, body2])
    body1.add_effect(gravity)
    body1.add_effect(stop_gravity)

    while True:
        engine.screen.fill(engine.options.BLACK)
        space.next_state()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        pg.display.flip()


if __name__ == "__main__":
    main()


