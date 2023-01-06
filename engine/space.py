import engine.node as node


class Space(node.Node):
    def __init__(self, pos: tuple[int, int]):
        super().__init__(pos)

        self.nodes = []

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