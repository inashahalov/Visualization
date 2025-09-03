import plotly.graph_objects as go

fig = go.Figure(data=[go.Bar(
    x=['Total', 'Used', 'Available', 'Cached', 'Buffers'],
    y=[15980, 9840, 5997, 8969, 187],
    marker_color=['blue', 'red', 'green', 'lightgreen', 'yellow']
)])
fig.update_layout(title='Memory Usage Distribution (MB)')
fig.show()