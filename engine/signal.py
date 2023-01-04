
class Signal:
    def __init__(self, node):
        self.node = node

    def activate(self, effect = None):
        if effect:
            self.node.add_effect(effect)

