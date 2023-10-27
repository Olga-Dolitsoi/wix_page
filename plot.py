import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Sample data
data = pd.DataFrame({
    'Date': pd.date_range(start='2023-01-01', end='2023-12-31', freq='D'),
    'Value': [i % 30 for i in range(365)]
})

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Date Range Chart with Dash and Plotly"),

    # Date Range Picker
    html.Div([
        dcc.DatePickerRange(
            id='date-picker-range',
            start_date=data['Date'].min(),
            end_date=data['Date'].max(),
            display_format='YYYY-MM-DD'
        )
    ]),

    # Plotly Chart
    dcc.Graph(id='line-chart')
])


@app.callback(
    Output('line-chart', 'figure'),
    [Input('date-picker-range', 'start_date'),
     Input('date-picker-range', 'end_date')]
)
def update_chart(start_date, end_date):
    filtered_data = data[(data['Date'] >= start_date) & (data['Date'] <= end_date)]

    fig = pl.e.line(filtered_data, x='Date', y='Value', title="Date Range Chart")

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
