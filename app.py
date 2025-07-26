## Cancer Genomics Dashboard Starter App
import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

# Load example dataset (replace with real genomics data)
data = pd.DataFrame({
    'Gene': ['TP53', 'BRCA1', 'EGFR', 'PIK3CA', 'KRAS'],
    'Mutations': [120, 90, 75, 60, 50]
})

# Initialize app
app = dash.Dash(__name__)

fig = px.bar(data, x='Gene', y='Mutations', title='Cancer Gene Mutations')

app.layout = html.Div(children=[
    html.H1(children='Cancer Genomics Dashboard'),
    html.P(children='Visualizing gene mutation data for cancer analysis.'),
    dcc.Graph(id='mutation-graph', figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)
