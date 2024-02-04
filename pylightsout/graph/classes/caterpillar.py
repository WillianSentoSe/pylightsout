from .. import Graph

class Caterpillar(Graph):
    def __init__(self, pattern=[]):
        super(Caterpillar, self).__init__()
        prev = None

        scale = max(pattern) / 2
        offset = len(pattern) * scale / 2.0

        for i, legs in enumerate(pattern):
            c = self.add_vertice('c', coord=((i * scale) - offset, 0))

            if (prev != None):
                self.add_edge(c, prev)
            
            for l in range(legs):
                ci = self.add_vertice(f'f', coord=(((i * scale) - (legs/2.0) + 0.5 + l) - offset, 1 if i%2 else -1))
                self.add_edge(c, ci)

            prev = c

