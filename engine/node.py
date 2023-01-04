import engine.init as init
import engine.effect as effect
import engine.signal as signal
import pygame as pg


class Node:
    def __init__(self, pos: tuple[int, int]):
        self.x = pos[0]
        self.y = pos[1]
        self.effects: set[effect.Effect] = set()
        self.signals: set[signal.Signal] = set()

    def next_state(self):
        for signal in self.signals:
            signal.activate(self)
        for effect in self.effects:
            effect.activate(self)

    def add_effect(self, effect: effect.Effect):
        self.effects.add(effect)

    def add_effects(self, effects: list[effect.Effect]):
        self.effects.update(effects)

    def send_effect(self, effect: effect.Effect, node):
        node.effects.add(effect)


class Body(Node):
    def __init__(self, pos: tuple[int, int], wight: int, height: int, color: tuple[int, int, int] = (255, 255, 255)):
        super().__init__(pos)

        self.wight = wight
        self.height = height

        self.color = color

    def render(self):

        rect = pg.Rect(self.x, self.y, self.wight, self.height)
        pg.draw.rect(init.screen, self.color, rect)