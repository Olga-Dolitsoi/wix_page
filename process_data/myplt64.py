import os

import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import dash_mantine_components as dmc
import plots as pl
import const as const


date = pl.convert_date(const.TABLE_NAME_PLOT71, const.TABLE_NAME_NAMES_PLOT71, const.LANG_LABELS_PLOT_71,
                       const.DATA_TABLE_COLUMNS_PLOT71, const.NAMES_TABLE_COLUMNS_PLOT71)
languages = ['ENG', 'UKR', 'RU']

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),  # Add dcc.Location to capture URL
    html.H1(id='name', style={'fontSize': 26, 'fontFamily': 'Montserrat'}),

# Date Range Picker
    html.Div([
        dmc.Group(
            children=[
                dmc.DatePicker(
                    id='start-date-picker',
                    label="Start Date",
                    inputFormat='MM/YYYY',  # Display format for Month and Year
                    minDate=date.min(),
                    maxDate=date.max(),
                    initialLevel='month',
                    style={"width": 200, 'fontFamily': 'Montserrat'}
                ),
                dmc.DatePicker(
                    id='end-date-picker',
                    label="End Date",
                    inputFormat='MM/YYYY',  # Display format for Month and Year
                    minDate=date.min(),
                    maxDate=date.max(),
                    initialLevel='month',
                    style={"width": 200, 'fontFamily': 'Montserrat'}
                ),
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
    [Input('start-date-picker', 'value'),
     Input('end-date-picker', 'value'),
     Input('language-dropdown', 'value')],
    [State('url', 'search')]

)
def update_chart(start_date, end_date, lang, url_search):
    url_lang = None
    url_start_date = None
    url_end_date = None
    if url_search:
        params = [param.split('=') for param in url_search[1:].split('&')]
        for param, value in params:
            if param == 'language-dropdown':
                url_lang = value
            elif param == 'start-date-picker':
                url_start_date = value
            elif param == 'end-date-picker':
                url_end_date = value

    # If the URL parameter is present, update the language dropdown and date pickers
    if url_lang and url_lang != lang:
        lang = url_lang

    if url_start_date:
        start_date = url_start_date

    if url_end_date:
        end_date = url_end_date
    fig, name, source = pl.build_plot71(lang=lang, start_date=start_date, end_date=end_date)

    return fig, name, source

@app.callback(
    Output('url', 'search'),
    [Input('start-date-picker', 'value'),
     Input('end-date-picker', 'value'),
     Input('language-dropdown', 'value')]
)
def update_url(start_date, end_date, lang):
    # Update the URL with the selected values
    url_params = []
    if start_date:
        url_params.append(f'start-date-picker={start_date}')
    if end_date:
        url_params.append(f'end-date-picker={end_date}')
    if lang:
        url_params.append(f'language-dropdown={lang}')

    return '?' + '&'.join(url_params)

try:
    ssh_con = os.getenv('SSH_CONNECTION').split(' ')[2]
except:
    ssh_con = None

my_port = 8115

if __name__ == '__main__':
    if ssh_con is not None:
        app.run_server(host='0.0.0.0',
                       port=my_port,
                       ssl_context=('/etc/letsencrypt/live/ueo-charts.com/fullchain.pem',
                                    '/etc/letsencrypt/live/ueo-charts.com/privkey.pem'))
    else:
        app.run_server(host='0.0.0.0', port=my_port)
