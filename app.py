import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Load processed data
df = pd.read_csv('processed_sales.csv')
df['date'] = pd.to_datetime(df['date'])

# Initialize Dash app
app = Dash(__name__)

# App layout
app.layout = html.Div(
    style={'textAlign': 'center', 'fontFamily': 'Arial', 'backgroundColor': '#f0f0f0', 'padding': '20px'},
    children=[
        html.H1(children='Pink Morsel Sales Visualiser', style={'color': '#333'}),
        
        html.Label('Select Region:', style={'fontSize': 20, 'marginRight': '10px'}),
        dcc.RadioItems(
            id='region-radio',
            options=[
                {'label': 'All', 'value': 'all'},
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'}
            ],
            value='all',
            inline=True,
            inputStyle={"marginRight": "5px", "marginLeft": "20px"}
        ),
        
        dcc.Graph(id='sales-line-chart')
    ]
)

# Callback to update chart based on region
@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-radio', 'value')
)
def update_chart(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'].str.lower() == selected_region.lower()]
    
    fig = px.line(filtered_df.sort_values('date'), x='date', y='Sales',
                  title=f'Pink Morsel Sales Over Time ({selected_region.capitalize()})',
                  labels={'date': 'Date', 'Sales': 'Total Sales ($)'})
    fig.update_layout(plot_bgcolor='#ffffff', paper_bgcolor='#f0f0f0')
    return fig

if __name__ == '__main__':
    app.run(debug=True)
