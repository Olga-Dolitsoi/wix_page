import os

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_mantine_components as dmc
import plots as pl
import const as const


date = pl.prepare_date_month_year(const.TABLE_NAME_PLOT14, const.TABLE_NAME_NAMES_PLOT14, const.LANG_LABELS_PLOT_14)
languages = ['ENG', 'UKR', 'RU']

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1(id='name', style={'fontSize': 26, 'fontFamily': 'Montserrat'}),

# Date Range Picker
    html.Div([
        dmc.Group(
            children=[
                dmc.DatePicker(
                    id='start-date-picker',
                    label="Start Date",
                    inputFormat='MM/YYYY',  # Display format for Month and Year
                    value=date.min(),  # Start from January 2023
                    minDate=date.min(),
                    maxDate=date.max(),
                    initialLevel='month',
                    style={"width": 200, 'fontFamily': 'Montserrat'}
                ),
                dmc.DatePicker(
                    id='end-date-picker',
                    label="End Date",
                    inputFormat='MM/YYYY',  # Display format for Month and Year
                    value=date.max(),  # End at December 2023
                    minDate=date.min(),
                    maxDate=date.max(),
                    initialLevel='month',
                    style={"width": 200, 'fontFamily': 'Montserrat'}
                )]
        )
    ]),
        dcc.Dropdown(
            id='language-dropdown',
            options=[{'label': lang, 'value': lang} for lang in languages],
            value='ENG',
            style={'width': 200, 'fontFamily': 'Montserrat'}),

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
     Input('language-dropdown', 'value')]
)
def update_chart(start_date, end_date, lang):
    fig, name, source = pl.build_plot14(lang=lang, start_date=start_date, end_date=end_date)

    return fig, name, source


try:
    ssh_con = os.getenv('SSH_CONNECTION').split(' ')[2]
except:
    ssh_con = None

my_port = 8060

if __name__ == '__main__':
    if ssh_con is not None:
        app.run_server(host='0.0.0.0',
                       port=my_port,
                       ssl_context=('/etc/letsencrypt/live/ueo-charts.com/fullchain.pem',
                                    '/etc/letsencrypt/live/ueo-charts.com/privkey.pem'))
    else:
        app.run_server(host='0.0.0.0', port=my_port)
