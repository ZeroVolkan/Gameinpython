import pygame as pg
import engine.options as options

clock = pg.time.Clock()
screen = pg.display.set_mode((options.WIDTH, options.HEIGHT))
pg.display.set_caption(options.NAME)