import pygame as pg
import options


pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((options.WIDTH, options.HEIGHT))
pg.display.set_caption(options.NAME)