import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import process_data.plots as pl
import process_data.const as const
import os



dates = pl.prepare_date_year_select_one(const.TABLE_NAME_PLOT2, const.TABLE_NAME_NAMES_PLOT2, const.LANG_LABELS_PLOT_2)
languages = ['ENG', 'UKR', 'RU']

app = dash.Dash(__name__)


app.layout = html.Div([
    html.H1(id='name'),

    # Date Range Picker
    html.Div([
        dcc.Dropdown(
            id='year_dropdown',
            options=[{'label': date, 'value': date} for date in dates],
            value=2023,
            style={'width': 200}
        ),
        dcc.Dropdown(
            id='language_dropdown',
            options=[{'label': lang, 'value': lang} for lang in languages],
            value='ENG',
            style={'width': 200}
        )
    ]),

    # Plotly Chart
    dcc.Graph(id='my-pie-chart'),
    html.Div(id='source', style={'font-style': 'italic'})
])


@app.callback(
    [Output('my-pie-chart', 'figure'),
     Output('name', 'children'),
     Output('source', 'children')],
    [Input('year_dropdown', 'value'),
     Input('language_dropdown', 'value')]
)
def update_chart(date, lang):
    fig, name, source = pl.build_plot_2(lang=lang, date=date)

    return fig, name, source


try:
    ssh_con = os.getenv('SSH_CONNECTION').split(' ')[2]
except:
    ssh_con = None

my_port = 8051

if __name__ == '__main__':

    if ssh_con is not None:
        app.run_server(host='0.0.0.0',
                        port=my_port,
                        ssl_context=('/etc/letsencrypt/live/ueo-charts.com/fullchain.pem',
                                        '/etc/letsencrypt/live/ueo-charts.com/privkey.pem'))
    else:
        app.run_server(host='0.0.0.0', port=my_port)
