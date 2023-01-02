from init import *
import pygame as pg


class Tile:
    def __init__(self, pos: tuple[int, int], color: tuple[int, int, int] = (255, 255, 255)):
        self.color = color
        self.pos = pos


class TileSet:
    def __init__(self, pos: tuple[int, int], tile: tuple[int, int], wight: int, height: int):
        self.wight = wight
        self.height = height
        self.pos = pos
        self.TileSet: list[list[Tile | None]] = [[None for w in range(wight)] for h in range(height)]
        self.tile = tile

    def add_object(self, tile: Tile):
        self.TileSet[tile.pos[1]][tile.pos[0]] = tile

    def get_real_pos(self, tile: Tile):
        return tile.pos[0] * self.tile[0] + self.pos[0], tile.pos[1] * self.tile[1] + self.pos[1]

    def render(self):
        for height in range(self.height):
            for wight in range(self.wight):
                tile = self.TileSet[height][wight]
                if tile is None:
                    continue
                if isinstance(tile, Tile):
                    real_pos = self.get_real_pos(tile)
                    rect = pg.Rect(real_pos[0], real_pos[1], self.tile[0], self.tile[1])
                    pg.draw.rect(screen, tile.color, rect)




