import os

import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import dash_mantine_components as dmc
import plots as pl
import const as const
min_year = 2010
max_year = 2023

date = pl.prepare_date_year_select_one_old(const.TABLE_NAME_PLOT54, const.TABLE_NAME_NAMES_PLOT54, const.LANG_LABELS_PLOT_54)

languages = ['ENG', 'UKR', 'RU']

external_stylesheets = [
    "https://fonts.googleapis.com/css?family=Montserrat:200,300,400,700",
    "https://fonts.googleapis.com/css?family=Open%20Sans"
]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),  # Add dcc.Location to capture URL
    html.H1(id='name', style={'fontSize': 26, 'fontFamily': 'Montserrat'}),

    html.Div([
        dmc.Group(
            children=[
                dmc.Select(id='min_year',
                           data=[{'label': dt, 'value': dt} for dt in date],
                           value=min_year,
                           style={'width': 200, 'fontFamily': 'Montserrat', 'margin-left': 0},
                           label='Start Date'),
                dmc.Select(id='max_year',
                           data=[{'label': dt, 'value': dt} for dt in date],
                           value=max_year,
                           style={'width': 200, 'fontFamily': 'Montserrat', 'margin-left': 0},
                           label='End Date')]
        ),
    ]),

    # Plotly Chart
    dcc.Graph(id='stacked-bar-chart'),
    html.Div(id='source', style={'font-style': 'italic', 'fontFamily': 'Montserrat'})
])


@app.callback(
    [Output('stacked-bar-chart', 'figure'),
     Output('name', 'children'),
     Output('source', 'children')],
    [Input('min_year', 'value'),
     Input('max_year', 'value')],
    [State('url', 'search')]

)
def update_chart(start_date, end_date, url_search):
    lang = None

    if url_search:
        params = [param.split('=') for param in url_search[1:].split('&')]
        for param, value in params:
            if param == 'language-dropdown':
                lang = value

    fig, name, source = pl.build_plot54(lang=lang, start_date=start_date, end_date=end_date)

    return fig, name, source


try:
    ssh_con = os.getenv('SSH_CONNECTION').split(' ')[2]
except:
    ssh_con = None

my_port = 8095

if __name__ == '__main__':
    if ssh_con is not None:
        app.run_server(host='0.0.0.0',
                       port=my_port,
                       ssl_context=('/etc/letsencrypt/live/ueo-charts.com/fullchain.pem',
                                    '/etc/letsencrypt/live/ueo-charts.com/privkey.pem'))
    else:
        app.run_server(host='0.0.0.0', port=my_port)
