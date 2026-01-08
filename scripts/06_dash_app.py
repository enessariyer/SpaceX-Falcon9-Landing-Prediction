from logging import PlaceHolder
from optparse import Values
import pandas as pd
import wget
import requests
import io
from dash import Dash, html, dcc, Input, Output
import plotly.graph_objects as go
import plotly.express as px


response = requests.get("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv")
s = response.content
df = pd.read_csv(io.StringIO(s.decode('utf-8')))

df['Booster Version'] = df['Booster Version'].str.extract(r'\s([\w.]+)')

app = Dash(__name__)

app.layout = html.Div([
    html.H1(
        'SpaceX Ingsights',
        style={'textAlign':'center', 'color':'503D36', 'font-size':'35px'}
        ),
    
    html.Div([
        html.Label('Select Site: ', style={'color':'blue', 'fontSize':'20px'}),
        dcc.Dropdown(
            id='site-dropdown',
            options=[
                {'label': 'Most Successful Launchs', 'value': 'ALL'},
                {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
                {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'},
                {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
                {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'},
            ],
            value='ALL',
            placeholder='Fırlatma Sahası Seçin',
            searchable=True
        )
    ], style={'padding':'10px'}
    ),
    
    html.Div([
            dcc.Graph(id='pie')
    ]),

    html.Div([
        dcc.RangeSlider(
            id='range-slider',
            min=0, max=10000, step=1000,
            value=[0, 10000],
            marks={0:'0', 2500:'2500', 5000:'5000', 7500:'7500', 10000:'10000'}
        )
    ]),

    html.Div([
        dcc.Graph(id='scatter')
    ])

])


@app.callback(
    [Output(component_id='pie', component_property='figure'),
     Output(component_id='scatter', component_property='figure')],
    [Input(component_id='site-dropdown', component_property='value'),
     Input(component_id='range-slider', component_property='value')]
)
def get_graph(site, payload_range):
    low, high = payload_range
    space_df = df[df['Payload Mass (kg)'].between(low, high)]

    if site == 'ALL':
        fig = px.pie(
            space_df, 
            values='class', 
            names='Launch Site', 
            title='Total Success by Site'
        )
        fig2 = px.scatter(
            space_df, 
            x='Payload Mass (kg)', 
            y='class', 
            color='Booster Version', 
            title='Correlation between Payload and Success for all Sites')
        return [fig, fig2]
    else:
        space_df_filtered = space_df[space_df['Launch Site'] == site]
        class_counts = space_df_filtered['class'].value_counts().reset_index()
        class_counts.columns = ['class', 'count']
        fig = px.pie(
            class_counts,
            values='count',
            names='class',
            title=f'Success (1) vs. Failure (0) for {site}'
        )
        fig2 = px.scatter(
            space_df_filtered,
            x='Payload Mass (kg)',
            y='class',
            color='Booster Version',
            title='Correlation between Payload and Success for all Sites'
        )
        return [fig, fig2]


if __name__ == '__main__':
    app.run(debug=True)