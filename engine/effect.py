class Effect:
    def __init__(self, name: str):
        self.name = name

    def activate(self, node):
        ...


class StopEffect(Effect):
    def __init__(self, name: str, stop_name: str):
        super().__init__(name)
        self.stop_name = stop_name

    def activate(self, node):
        node.del_effect(self.stop_name)


class StopEffectIfSignal(StopEffect):
    def __init__(self, name: str, stop_name: str, signal: str):
        super().__init__(name, stop_name)
        self.signal = signal

    def activate(self, node):
        if node.signals.get(self.signal):
            node.del_effect(self.stop_name)


class Gravity(Effect):
    def activate(self, node):
        node.y += 10


