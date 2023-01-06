import engine.node as node
import engine.space as space
import engine.signal as signal
import engine.effect as effect


class Collision(effect.Effect):
    def body(self, body1: node.Body, body2: node.Body):
        if body1.x + body1.wight < body2.x:
            return False
        if body1.x > body2.wight + body2.x:
            return False
        if body1.y > body2.wight + body2.y:
            return False
        if body1.y + body1.height < body2.y:
            return False
        return True

    def activate(self, space: space.Space):
        ln = len(space.nodes)
        for i in range(ln):
            for j in range(i + 1, ln):
                if self.body(space.nodes[i], space.nodes[j]):
                    space.nodes[i].add_signal(
                        signal.Signal(space.nodes[j], name=self.name)
                    )
                    space.nodes[j].add_signal(
                        signal.Signal(space.nodes[i], name=self.name)
                    )