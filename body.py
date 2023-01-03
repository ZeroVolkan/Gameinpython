from init import *
import pygame as pg


class Body:
    def __init__(self, pos: tuple[int, int], wight: int, height: int, color: tuple[int, int, int] = (255, 255, 255)):
        self.pos = pos
        self.wight = wight
        self.height = height
        self.color = color

    def render(self):
        rect = pg.Rect(self.pos[0], self.pos[1], self.wight, self.height)
        pg.draw.rect(screen, self.color, rect)


class Collision:
    def __init__(self):
        self.events = []

    def body(self, body1: Body, body2: Body):
        if body1.pos[0] + body1.wight < body2.pos[0]:
            return False
        if body1.pos[0] > body2.wight + body2.pos[0]:
            return False
        if body1.pos[1] > body2.wight + body2.pos[1]:
            return False
        if body1.pos[1] + body1.height < body2.pos[1]:
            return False
        return True
