import engine.node as node
import engine.space as space


class Collision:
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
            for j in range(ln - i):
                self.body(space.nodes[i + j], space.nodes[j])
