import plotly.graph_objects as go

fig = go.Figure(data=[go.Table(
                header=dict(
                    values=['', 'Condorcet', 'Borda', 'IRV'],
                    fill_color='lightgray',
                    ),
                cells=dict(
                    values=[['Plurality', 'Condorcet', 'Borda'], [], [], []], 
                    fill=dict(color=['lightgray', 'white', 'white', 'white'])), 
                    )
                ])
fig.show()