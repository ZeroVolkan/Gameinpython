import engine.init as init
import engine.effect as effect
import engine.signal
import engine.signal as signal
import pygame as pg


class Node:
    def __init__(self, pos: tuple[int, int]):
        self.x = pos[0]
        self.y = pos[1]
        self.effects: dict[str, effect.Effect] = dict()
        self.signals: dict[str, signal.Signal] = dict()
        self.stopping: list[str] = list()

    def next_state(self):
        for signal in self.signals.values():
            signal.activate(self)
        for effect in self.effects.values():
            effect.activate(self)
        self.signals.clear()
        for stop in self.stopping:
            if self.effects.get(stop):
                del self.effects[stop]


    def add_effect(self, effect: effect.Effect):
        self.effects.setdefault(effect.name, effect)

    def add_effects(self, effects: list[effect.Effect]):
        for effect in effects:
            self.add_effect(effect)

    def del_effect(self, effect: effect.Effect | str):
        if isinstance(effect, str):
            self.stopping.append(effect)
        else:
            self.stopping.append(effect.name)

    def del_effects(self, effects: list[effect.Effect]):
        for effect in effects:
            self.del_effect(effect)

    def add_signal(self, signal):
        self.signals.setdefault(signal.name, signal)

    def add_signals(self, signals):
        for signal in signals:
            self.add_signal(signal)


class Body(Node):
    def __init__(self, pos: tuple[int, int], wight: int, height: int, color: tuple[int, int, int] = (255, 255, 255)):
        super().__init__(pos)

        self.wight = wight
        self.height = height

        self.color = color

    def render(self):

        rect = pg.Rect(self.x, self.y, self.wight, self.height)
        pg.draw.rect(init.screen, self.color, rect)

