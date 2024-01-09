import os

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plots as pl
import const as const


dates = pl.prepare_date_year_select_one(const.TABLE_NAME_PLOT9, const.TABLE_NAME_NAMES_PLOT9, const.LANG_LABELS_PLOT_9)
languages = ['ENG', 'UKR', 'RU']

# Sample data

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1(id='name'),

    # Date Range Picker
    html.Div([
        dcc.Dropdown(
            id='year_dropdown',
            options=[{'label': date, 'value': date} for date in dates],
            value=2023,
            style={"width": 200}
        ),
        dcc.Dropdown(
            id='language_dropdown',
            options=[{'label': lang, 'value': lang} for lang in languages],
            value='ENG',
            style={"width": 200}
        )
    ]),

    # Plotly Chart
    dcc.Graph(id='stacked_bar_chart'),
    html.Div(id='source', style={'font-style': 'italic'})
])


@app.callback(
    [Output('stacked_bar_chart', 'figure'),
     Output('name', 'children'),
     Output('source', 'children')],
    [Input('year_dropdown', 'value'),
     Input('language_dropdown', 'value')]
)
def update_chart(year, lang):
    fig, name, source = pl.build_plot9(lang=lang, date=year)
    return fig, name, source


try:
    ssh_con = os.getenv('SSH_CONNECTION').split(' ')[2]
except:
    ssh_con = None

my_port = 8055

if __name__ == '__main__':
    if ssh_con is not None:
        app.run_server(host='0.0.0.0',
                       port=my_port,
                       ssl_context=('/etc/letsencrypt/live/ueo-charts.com/fullchain.pem',
                                    '/etc/letsencrypt/live/ueo-charts.com/privkey.pem'))
    else:
        app.run_server(host='0.0.0.0', port=my_port)
