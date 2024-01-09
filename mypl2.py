import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_mantine_components as dmc
import datetime
import process_data.const as const
import process_data.plots as pl
import os


date = pl.prepare_date_month_year(const.TABLE_NAME_PLOT3, const.TABLE_NAME_NAMES_PLOT3, const.LANG_LABELS_PLOT_3)
languages = ['ENG', 'UKR', 'RU']

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1(id='name'),

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
                    maxDate=date.max()+datetime.timedelta(hours=12),
                    initialLevel='month',
                    style={"width": 200}
                ),
                dmc.DatePicker(
                    id='end-date-picker',
                    label="End Date",
                    inputFormat='MM/YYYY',  # Display format for Month and Year
                    value=date.max(),  # End at December 2023
                    minDate=date.min(),
                    maxDate=date.max()+datetime.timedelta(hours=12),
                    initialLevel='month',
                    style={"width": 200}
                )]
        )
    ]),
        dcc.Dropdown(
            id='language-dropdown',
            options=[{'label': lang, 'value': lang} for lang in languages],
            value='ENG',
            style={'width': 200}),

    # Plotly Chart
    dcc.Graph(id='grouped-stacked-bar-chart'),
    html.Div(id='source', style={'font-style': 'italic'})
])


@app.callback(
    [Output('grouped-stacked-bar-chart', 'figure'),
     Output('name', 'children'),
     Output('source', 'children')],
    [Input('start-date-picker', 'value'),
     Input('end-date-picker', 'value'),
     Input('language-dropdown', 'value')]
)
def update_chart(start_date, end_date, lang):
    fig, name, source = pl.build_plot_3(lang=lang, start_date=start_date, end_date=end_date)

    return fig, name, source


try:
    ssh_con = os.getenv('SSH_CONNECTION').split(' ')[2]
except:
    ssh_con = None

my_port = 8052

if __name__ == '__main__':
    if ssh_con is not None:
        app.run_server(host='0.0.0.0',
                        port=my_port,
                        ssl_context=('/etc/letsencrypt/live/ueo-charts.com/fullchain.pem',
                                        '/etc/letsencrypt/live/ueo-charts.com/privkey.pem'))
    else:
        app.run_server(host='0.0.0.0', port=my_port)