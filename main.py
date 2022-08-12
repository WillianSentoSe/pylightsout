from graph import Graph

G = Graph()

v1 = G.add_vertice(coord=(1, 0))
v2 = G.add_vertice(coord=(0, 1), N=[v1])
v3 = G.add_vertice(coord=(-1, 0), N=[v2])
v4 = G.add_vertice(coord=(0, -1), N=[v3, v1])
v5 = G.add_vertice(coord=(2, 0), N=[v1])
v6 = G.add_vertice(coord=(3, 0), N=[v5])
v7 = G.add_vertice(coord=(4, 0), N=[v6])

G.press(v1)
G.press(v2)
G.press(v3)
G.press(v4)
G.press(v7)

G.plot()