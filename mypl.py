import os

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import process_data.plots as pl
import process_data.const as const
import pandas as pd


date_0 = pl.prepare_date_month_year_full(const.TABLE_NAME_PLOT1, const.TABLE_NAME_NAMES_PLOT1, const.LANG_LABELS_PLOT_1)
date_0 = date_0.loc[(date_0[date_0.columns.difference(['index_0', 'index_1', 'id'])] !=0).any(axis=1)]
date = pd.to_datetime(
        (date_0['index_0'].astype(int)).astype(str) + '-' + (date_0['index_1'].astype(int)).astype(str),
        format='%Y-%m')

languages = ['ENG', 'UKR', 'RU']

# Sample data

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1(id='name'),

    # Date Range Picker
    html.Div([
        dcc.DatePickerSingle(
            id='start-date-picker',
            display_format='MM/YYYY',  # Display format for Month and Year
            date=date.min(),  # Start from January 2023
            min_date_allowed=date.min(),
            max_date_allowed=date.max(),
            style={'width': 200}
        ),
        dcc.DatePickerSingle(
            id='end-date-picker',
            display_format='MM/YYYY',  # Display format for Month and Year
            date=date.max(),  # End at December 2023
            min_date_allowed=date.min(),
            max_date_allowed=date.max(),
            style={'with': 200}
        ),
        dcc.Dropdown(
            id='language-dropdown',
            options=[{'label': lang, 'value': lang} for lang in languages],
            value='ENG',
            style={'width': 200}
        ),
    ]),

    # Plotly Chart
    dcc.Graph(id='stacked-bar-chart'),
    html.Div(id='source', style={'font-style': 'italic'})
])


@app.callback(
    [Output('stacked-bar-chart', 'figure'),
     Output('name', 'children'),
     Output('source', 'children')],
    [Input('start-date-picker', 'date'),
     Input('end-date-picker', 'date'),
     Input('language-dropdown', 'value')]
)
def update_chart(start_date, end_date, value):
    fig, name, source = pl.build_plot_1(lang=value, start_date=start_date, end_date=end_date)
    return fig, name, source


try:
    ssh_con = os.getenv('SSH_CONNECTION').split(' ')[2]
except:
    ssh_con = None

my_port = 8050

if __name__ == '__main__':
    if ssh_con is not None:
        app.run_server(host='0.0.0.0',
                       port=my_port,
                       ssl_context=('/etc/letsencrypt/live/ueo-charts.com/fullchain.pem',
                                    '/etc/letsencrypt/live/ueo-charts.com/privkey.pem'))
    else:
        app.run_server(host='0.0.0.0', port=my_port)