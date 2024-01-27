import os

import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import dash_mantine_components as dmc
import plots as pl
import const as const

date = pl.prepare_date_year_select_one(const.TABLE_NAME_PLOT70, const.TABLE_NAME_NAMES_PLOT70,
                                       const.LANG_LABELS_PLOT_70)

languages = ['ENG', 'UKR', 'RU']

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),  # Add dcc.Location to capture URL
    html.H1(id='name', style={'fontSize': 26, 'fontFamily': 'Montserrat'}),


    html.Div([
        dmc.Group(
            children=[
                dmc.Select(id='year',
                           data=[{'label': dt, 'value': dt} for dt in date],
                           style={'width': 200, 'fontFamily': 'Montserrat', 'margin-left': 0},
                           label='Language'),
                dmc.Select(id='language-dropdown',
                           data=[{'label': lang, 'value': lang} for lang in languages],
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
     ],
    [State('url', 'search')]

)
def update_chart(year, lang, url_search):
    url_year = None
    url_lang = None

    if url_search:
        params = [param.split('=') for param in url_search[1:].split('&')]
        for param, value in params:
            if param == 'one-year':
                url_year = int(value)
            elif param == 'language-dropdown':
                url_lang = value

    # If the URL parameter is present, update the year and language dropdowns
    if url_year and url_year != year:
        year = url_year

    if url_lang and url_lang != lang:
        lang = url_lang
    fig, name, source = pl.build_plot70(lang=lang, date=year)

    return fig, name, source

@app.callback(
    Output('url', 'search'),
    [Input('one-year', 'value'),
     Input('language-dropdown', 'value')]
)
def update_url(year, lang):
    # Update the URL with the selected year and language
    url_params = []
    if year:
        url_params.append(f'one-year={year}')
    if lang:
        url_params.append(f'language-dropdown={lang}')

    return '?' + '&'.join(url_params)


try:
    ssh_con = os.getenv('SSH_CONNECTION').split(' ')[2]
except:
    ssh_con = None

my_port = 8114

if __name__ == '__main__':
    if ssh_con is not None:
        app.run_server(host='0.0.0.0',
                       port=my_port,
                       ssl_context=('/etc/letsencrypt/live/ueo-charts.com/fullchain.pem',
                                    '/etc/letsencrypt/live/ueo-charts.com/privkey.pem'))
    else:
        app.run_server(host='0.0.0.0', port=my_port)
