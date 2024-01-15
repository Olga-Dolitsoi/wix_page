import os

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_mantine_components as dmc
import plots as pl
import const as const

quoter = pl.get_quoter(const.TABLE_NAME_PLOT44, const.TABLE_NAME_NAMES_PLOT44, const.LANG_LABELS_PLOT_44)
date = pl.prepare_date_year_select_one(const.TABLE_NAME_PLOT44, const.TABLE_NAME_NAMES_PLOT44,
                                       const.LANG_LABELS_PLOT_44)

languages = ['ENG', 'UKR', 'RU']

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1(id='name', style={'fontSize': 26, 'fontFamily': 'Montserrat'}),


    html.Div([
        dmc.Group(
            children=[
                dmc.Select(id='min_year',
                           data=[{'label': dt, 'value': dt} for dt in date],
                           value=date.min(),
                           style={'width': 200, 'fontFamily': 'Montserrat', 'margin-left': 0},
                           label='Min Year'),
                dmc.Select(id='max_year',
                           data=[{'label': dt, 'value': dt} for dt in date],
                           value=date.max(),
                           style={'width': 200, 'fontFamily': 'Montserrat', 'margin-left': 0},
                           label='Max Year'),
                dmc.Select(id='language-dropdown',
                           data=[{'label': lang, 'value': lang} for lang in languages],
                           value='ENG',
                           style={'width': 200, 'fontFamily': 'Montserrat', 'margin-left': 50},
                           label='Language')])]),
    # html.Div([
    #     dmc.Group(
    #         children=[
    #             dmc.Select(id='min_quoter',
    #                        data=[{'label': quot, 'value': quot} for quot in quoter],
    #                        value=quoter.min(),
    #                        style={'width': 200, 'fontFamily': 'Montserrat', 'margin-left': 50},
    #                        label='Min Quoter'),
    #             dmc.Select(id='max_quoter',
    #                        data=[{'label': quot, 'value': quot} for quot in quoter],
    #                        value=quoter.max(),
    #                        style={'width': 200, 'fontFamily': 'Montserrat', 'margin-left': 50},
    #                        label='Max Quoter'),
    #         ]
    #     )
    # ]),

    # Plotly Chart
    dcc.Graph(id='stacked-bar-chart'),
    html.Div(id='source', style={'font-style': 'italic', 'fontFamily': 'Montserrat'})
])


@app.callback(
    [Output('stacked-bar-chart', 'figure'),
     Output('name', 'children'),
     Output('source', 'children')],
    [Input('min_year', 'value'),
     Input('max_year', 'value'),
     Input('language-dropdown', 'value')
     # Input('min_quoter', 'value'),
     # Input('max_quoter', 'value')
     ]
)
def update_chart(min_year, max_year, lang):
    fig, name, source = pl.build_plot44(lang=lang, min_year=min_year, max_year=max_year)

    return fig, name, source


try:
    ssh_con = os.getenv('SSH_CONNECTION').split(' ')[2]
except:
    ssh_con = None

my_port = 8086

if __name__ == '__main__':
    if ssh_con is not None:
        app.run_server(host='0.0.0.0',
                       port=my_port,
                       ssl_context=('/etc/letsencrypt/live/ueo-charts.com/fullchain.pem',
                                    '/etc/letsencrypt/live/ueo-charts.com/privkey.pem'))
    else:
        app.run_server(host='0.0.0.0', port=my_port)