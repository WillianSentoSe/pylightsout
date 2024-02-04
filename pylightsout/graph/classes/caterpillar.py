from .. import Graph

class Caterpillar(Graph):
    def __init__(self, legs_pattern=[], spine_prefix='v', leg_prefix='u'):
        super(Caterpillar, self).__init__()

        self.spine_prefix = spine_prefix
        self.leg_prefix = leg_prefix

        prev = None

        scale = max(1, max(legs_pattern) / 2)
        offset = len(legs_pattern) * scale / 2.0

        for i, legs in enumerate(legs_pattern):
            c = self.add_vertice(spine_prefix, coord=((i * scale) - offset, 0))

            if (prev != None):
                self.add_edge(c, prev)
            
            for l in range(legs):
                ci = self.add_vertice(leg_prefix, coord=(((i * scale) - (legs/2.0) + 0.5 + l) - offset, 1 if i%2 else -1))
                self.add_edge(c, ci)

            prev = c

    def spine(self):
        return self.subgraph(lambda v: v.startswith(self.spine_prefix))
