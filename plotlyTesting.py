import plotly.graph_objects as go
import plotly.colors as pc
import numpy as np

colours = pc.n_colors('rgb(255, 200, 200)', 'rgb(180, 0, 0)', 101, colortype='rgb')

vals = [[10.8, '', ''], [50.2, 25.4, ''], [100.0, 40.4, 75.1]]
a = int((vals[0])[0])
b = int((vals[1])[0])
c = int((vals[1])[1])
d = int((vals[2])[0])
e = int((vals[2])[1])
f = int((vals[2])[2])

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
fig.update_layout(width=1000, height=1000)
fig.show()