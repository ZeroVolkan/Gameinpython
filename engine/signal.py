class Signal:
    def __init__(self, node, name: str = ""):
        self.name = name
        self.node = node

    def activate(self, node, effect=None):
        if effect:
            self.node.add_effect(effect)

