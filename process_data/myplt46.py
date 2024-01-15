import os

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_mantine_components as dmc
import plots as pl
import const as const

date = pl.prepare_date_year_select_one(const.TABLE_NAME_PLOT56, const.TABLE_NAME_NAMES_PLOT56, const.LANG_LABELS_PLOT_56)

languages = ['ENG', 'UKR', 'RU']

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1(id='name', style={'fontSize': 26, 'fontFamily': 'Montserrat'}),


    html.Div([
        dmc.Group(
            children=[
                dmc.Select(id='year',
                           data=[{'label': dt, 'value': dt} for dt in date],
                           value=date.min(),
                           style={'width': 200, 'fontFamily': 'Montserrat', 'margin-left': 0},
                           label='Language'),
                dmc.Select(id='language-dropdown',
                           data=[{'label': lang, 'value': lang} for lang in languages],
                           value='ENG',
                           style={'width': 200, 'fontFamily': 'Montserrat', 'margin-left': 50},
                           label='Language')]
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
    [Input('year', 'value'),
     Input('language-dropdown', 'value')
     ]
)
def update_chart(year, lang):
    fig, name, source = pl.build_plot56(lang=lang, year=year)

    return fig, name, source


try:
    ssh_con = os.getenv('SSH_CONNECTION').split(' ')[2]
except:
    ssh_con = None

my_port = 8097

if __name__ == '__main__':
    if ssh_con is not None:
        app.run_server(host='0.0.0.0',
                       port=my_port,
                       ssl_context=('/etc/letsencrypt/live/ueo-charts.com/fullchain.pem',
                                    '/etc/letsencrypt/live/ueo-charts.com/privkey.pem'))
    else:
        app.run_server(host='0.0.0.0', port=my_port)
