import plotly.graph_objects as go

def plot_vertices(G, fig, nodesize=0.3, highlightmove=False):

    for v in G.V:
        on = G.C[v] == 1
        pressed = G.P[v]
        highlighted = highlightmove and G.x == v
        x, y = G.coord[v]

        fig.add_annotation(
            go.layout.Annotation(
                text=v,
                x=x,
                y=y,
                showarrow=False,
                font={
                    "color": "black" if on else "white",
                }
            )
        )

        fig.add_shape(
            type="circle",
            name=v,
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

def plot_graph(G, padding=1, nodesize=0.25, highlightmove=False, size=(1200, 600), grid=True):
    width, height = size
    fig = go.Figure()

    fig.update_xaxes(range=[-G.n - padding, G.n + padding])
    fig.update_yaxes(scaleanchor = "x", scaleratio = 1)

    plot_vertices(G, fig, nodesize=nodesize, highlightmove=highlightmove)

    fig.update_layout(
        width=width,
        height=height,
        plot_bgcolor="white",
        margin=dict(l=0, r=0, t=0, b=0),
        xaxis=dict(visible=grid, showgrid=True, dtick=1, gridcolor="#F4F4F4", scaleanchor="y", scaleratio=1, range=[-6, 6], layer='below traces', zeroline=False),  # Ajusta a escala do eixo X
        yaxis=dict(visible=grid, showgrid=True, dtick=1, gridcolor="#F4F4F4", scaleanchor="x", scaleratio=1, range=[-6, 6], layer='below traces', zeroline=False),  # Ajusta a escala do eixo Y
    )

    fig.show()