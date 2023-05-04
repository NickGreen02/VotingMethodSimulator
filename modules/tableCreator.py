import plotly.graph_objects as go
import plotly.colors as pc
import numpy as np

def create_table(vals):
    colours = pc.n_colors('rgb(255, 210, 210)', 'rgb(190, 0, 0)', 101, colortype='rgb')

    a = round(int(float((vals[0])[0])))
    b = round(int(float((vals[1])[0])))
    c = round(int(float((vals[1])[1])))
    d = round(int(float((vals[2])[0])))
    e = round(int(float((vals[2])[1])))
    f = round(int(float((vals[2])[2])))

    fig = go.Figure(data=[go.Table(
                    header=dict(
                        values=['', 'Condorcet', 'Borda', 'IRV'],
                        fill_color='gray',
                        font=dict(color='white', size=24),
                        height=40
                        ),
                    cells=dict(
                        values=[
                            ['Plurality', 'Condorcet', 'Borda'],
                            [str((vals[0])[0]) + "%", "", ""],
                            [str((vals[1])[0]) + "%", str((vals[1])[1]) + "%", ""],
                            [str((vals[2])[0]) + "%", str((vals[2])[1]) + "%", str((vals[2])[2]) + "%"]
                            ],
                        fill_color=[
                            'gray',
                            [np.array(colours)[a], 'white', 'white'],
                            [np.array(colours)[b], np.array(colours)[c], 'white'],
                            [np.array(colours)[d], np.array(colours)[e], np.array(colours)[f]]
                            ],
                        font=dict(color='white', size=24),
                        height=40
                        )
                    )
                ])
    fig.update_layout(width=1000, height=1000, title="Disagreement Table")
    fig.show()
