from init import *
import pygame as pg


class Tile:
    def __init__(self, color: tuple[int, int, int] = (255, 255, 255)):
        self.color = color

class TileSet:
    def __init__(self, pos: tuple[int, int], tile: tuple[int, int]):
        self.pos = pos
        self.TileSet: dict = {}
        self.tile = tile

    def add_object(self, tile: Tile, pos: tuple[int, int]):
        self.TileSet[pos] = tile

    def get_real_pos(self, pos: tuple[int, int]):
        return pos[0] * self.tile[0], pos[1] * self.tile[1]

    def render(self):
        for pos, tile in self.TileSet.items():
            real_pos = self.get_real_pos(pos)
            rect = pg.Rect(real_pos[0], real_pos[1], self.tile[0], self.tile[1])
            pg.draw.rect(screen, tile.color, rect)



