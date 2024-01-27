import os

import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import dash_mantine_components as dmc
import plots as pl
import const as const


languages = ['ENG', 'UKR', 'RU']

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),  # Add dcc.Location to capture URL
    html.H1(id='name', style={'fontSize': 26, 'fontFamily': 'Montserrat'}),


    html.Div([
        dmc.Group(
            children=[
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
    [Input('language-dropdown', 'value')],
    [State('url', 'search')]

)
def update_chart(lang, url_search):
    url_lang = None
    if url_search:
        url_lang_param = [param.split('=') for param in url_search[1:].split('&') if 'lang' in param]
        if url_lang_param:
            url_lang = url_lang_param[0][1]

    if url_lang and url_lang != lang:
        lang = url_lang
    fig, name, source = pl.build_plot11(lang)

    return fig, name, source


@app.callback(
    Output('url', 'search'),
    [Input('language-dropdown', 'value')]
)
def update_url(lang):
    # Update the URL with the selected language
    return f'?language-dropdown={lang}'


try:
    ssh_con = os.getenv('SSH_CONNECTION').split(' ')[2]
except:
    ssh_con = None

my_port = 8057

if __name__ == '__main__':
    if ssh_con is not None:
        app.run_server(host='0.0.0.0',
                       port=my_port,
                       ssl_context=('/etc/letsencrypt/live/ueo-charts.com/fullchain.pem',
                                    '/etc/letsencrypt/live/ueo-charts.com/privkey.pem'))
    else:
        app.run_server(host='0.0.0.0', port=my_port)

