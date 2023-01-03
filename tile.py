from init import *
from body import *
import pygame as pg


class Tile:
    def __init__(self, pos: tuple[int, int], color: tuple[int, int, int] = (255, 255, 255)):
        self.pos = pos
        self.color = color


class TileSet:
    def __init__(self, pos: tuple[int, int], tile_size: tuple[int, int], collision: bool = True):
        self.pos = pos
        self.TileSet = set()
        self.tile_size = tile_size
        self.collision = collision

    def add_tile(self, tile: Tile):
        self.TileSet.add(tile)

    def get_real_pos(self, pos: tuple[int, int]):
        return pos[0] * self.tile_size[0], pos[1] * self.tile_size[1]

    def render(self):
        for tile in self.TileSet:
            real_pos = self.get_real_pos(tile.pos)
            rect = pg.Rect(real_pos[0], real_pos[1], self.tile_size[0], self.tile_size[1])
            pg.draw.rect(screen, tile.color, rect)


def tile_constructor(color: tuple[int, int, int]):
    def tile(pos: tuple[int, int]):
        return Tile(pos, color)

    return tile
