from init import *
from body import *
import pygame as pg


class Tile:
    def __init__(self, pos: tuple[int, int], color: tuple[int, int, int] = (255, 255, 255)):
        self.pos = pos
        self.color = color


class TileSet:
    def __init__(self, pos: tuple[int, int],  wight_tile: int, height_tile: int, collision: bool = True):
        self.pos = pos
        self.TileSet = set()
        self.wight_tile = wight_tile
        self.height_tile = height_tile
        self.collision = collision

    def add_tile(self, tile: Tile):
        self.TileSet.add(tile)

    def get_real_pos(self, pos: tuple[int, int]):
        return pos[0] * self.wight_tile, pos[1] * self.height_tile

    def render(self):
        for tile in self.TileSet:
            real_pos = self.get_real_pos(tile.pos)
            rect = pg.Rect(real_pos[0], real_pos[1], self.wight_tile, self.height_tile)
            pg.draw.rect(screen, tile.color, rect)


def tile_constructor(color: tuple[int, int, int]):
    def tile(pos: tuple[int, int]):
        return Tile(pos, color)

    return tile
