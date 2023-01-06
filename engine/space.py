import engine.node as node
import pygame as pg


class Space(node.Node):
    def __init__(self, pos: tuple[int, int], wight: int, height: int, flipped: bool = True, name: str = "",
                 fps: int = 30):
        super().__init__(pos)
        self.name = name

        self.wight = wight
        self.height = height
        self.flipped = flipped

        self.nodes = []

        self.clock = pg.time.Clock()
        self.FPS = fps
        self.screen = pg.display.set_mode((self.wight, self.height))
        pg.display.set_caption(self.name)

    def add_node(self, node: node.Node):
        self.nodes.append(node)

    def add_nodes(self, nodes: list[node.Node]):
        self.nodes.extend(nodes)

    def next_state(self):
        for signal in self.signals.values():
            signal.activate(self)
        for effect in self.effects.values():
            effect.activate(self)
        for node in self.nodes:
            node.next_state()
        self.signals.clear()
        for stop in self.stopping:
            del self.effects[stop]
        self.clock.tick(self.FPS)
