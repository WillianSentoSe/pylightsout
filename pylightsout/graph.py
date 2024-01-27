from .plot import plot_graph
from .solver import brute_force
import random
import math

class Graph:

    def __init__(self, V=[], E=[], N={}, coord = {}):
        self.V = V
        self.E = E
        self.N = N
        self.n = len(V)
        self.m = len(E)
        self.coord = coord
        self.C = {}
        self.P = {}

        self.reset()

    def add_vertice(self, prefix="v", coord=(0, 0), N=[]):
        v = prefix + str(self.n)

        self.V.append(v)
        self.n += 1
        self.N[v] = []
        self.C[v] = 0
        self.P[v] = False
        self.coord[v] = coord

        for u in N:
            self.add_edge(v, u)

        return v

    def add_edge(self, v1, v2):
        if (v1, v2) not in self.E and (v2, v1) not in self.E:
            self.N[v1].append(v2)
            self.N[v2].append(v1)
            self.E.append((v1, v2))

    def reset(self):
        self.x = None
        self.X = []

        for v in self.V:
            self.C[v] = 0
            self.P[v] = False

    def check(self):
        for v in self.V:
            if (self.C[v] == 0):
                return False
        return True

    def switch(self, v):
        self.C[v] = 1 if self.C[v] == 0 else 0

    def press(self, v):
        self.switch(v)
        self.P[v] = not self.P[v]
        self.x = v
        
        if (self.P[v]):
            self.X.append(v)
        else:
            self.X.remove(v)

        for n in self.N[v]:
            self.switch(n)

    def plot(self, X=None, grid=True, size=(1200, 600)):
        if (X != None):
            self.reset()
            for v in X:
                self.press(v)

        plot_graph(self, grid=grid, size=size)

    def solve(self, method="brute_force"):
        S = None

        if (method == "brute_force"):
            S = brute_force(self)
        else:
            raise Exception("Method not found")
        
        self.reset()
        return S

def from_adjdict(N, coord={}):
    V = list(N.keys())
    E = list()

    for v1 in V:
        for v2 in N[v1]:
            if (v1, v2) not in E and (v2, v1) not in E:
                E.append((v1, v2))

    return Graph(V, E, N, coord)

def create_random(nodes, edges=None, prefix="v"):
    max_edges = edges if edges != None else (nodes - 1)
    edge_count = 0
    coord = {}
    N = {}

    for i in range(0, nodes):
        v = prefix + str(i)
        N[v] = []

        angle = math.radians((i / nodes) * 360.0)
        x = math.sin(angle) * nodes
        y = math.cos(angle) * nodes
        coord[v] = (x, y)

    while (edge_count < max_edges):
        start = prefix + str(random.randrange(0, nodes))
        end = prefix + str(random.randrange(0, nodes))

        if (start != end and end not in N[start]):
            N[start].append(end)
            N[end].append(start)
            edge_count += 1

    return from_adjdict(N, coord)
