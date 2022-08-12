import plotly.graph_objects as go
import math

def plot_vertices(G, fig, nodesize=0.25, highlightmove=False):

    for v in G.V:
        on = G.C[v] == 1
        pressed = G.P[v]
        highlighted = highlightmove and G.x == v
        x, y = G.coord[v]

        fig.add_shape(
            type="circle",
            xref="x", yref="y",
            x0=x - nodesize,
            y0=y - nodesize,
            x1=x + nodesize,
            y1=y + nodesize,
            fillcolor="white" if on else "gray",
            line_color="Red" if pressed else "Gray",
            line={ "width": 3 if highlighted else 2 },
        )

    for (v0, v1) in G.E:
        active = G.P[v0] or G.P[v1]
        highlighted = highlightmove and (G.x == v0 or G.x == v1)
        x0, y0 = G.coord[v0]
        x1, y1 = G.coord[v1]

        fig.add_shape(
            type="line",
            xref="x", yref="y",
            x0=x0, y0=y0,
            x1=x1, y1=y1,
            line_color="lightpink" if active else "lightgray",
            line={ "width": 3 if highlighted else 2 },
            layer="below",
        )

def plot_graph(G, padding=1, nodesize=0.25, highlightmove=False, size=(500, 500)):
    width, height = size
    fig = go.Figure()

    fig.update_xaxes(range=[-G.n - padding, G.n + padding])
    fig.update_yaxes(scaleanchor = "x", scaleratio = 1)

    plot_vertices(G, fig, nodesize=nodesize, highlightmove=highlightmove)

    fig.update_layout(
        width=width,
        height=height,
        xaxis={ "visible": False },
        yaxis={ "visible": False },
        plot_bgcolor="White"
    )

    fig.show()