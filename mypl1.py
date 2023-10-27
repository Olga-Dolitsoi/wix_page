import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Sample data
data = pd.DataFrame({
    'Date': pd.date_range(start='2023-01-01', end='2023-12-31', freq='D'),
    'Value': [i % 20 for i in range(365)]
})

app = dash.Dash(__name__)


app.layout = html.Div([
    html.H1("Stacked Bar Chart with Date Range Picker"),

    # Date Range Picker
    html.Div([
        dcc.DatePickerSingle(
            id='start-date-picker',
            display_format='MM/YYYY',  # Display format for Month and Year
            date=data['Date'].min(),  # Start from January 2023
            min_date_allowed=data['Date'].min(),
            max_date_allowed=data['Date'].max()
        ),
        dcc.DatePickerSingle(
            id='end-date-picker',
            display_format='MM/YYYY',  # Display format for Month and Year
            date=data['Date'].max(),  # End at December 2023
            min_date_allowed=data['Date'].min(),
            max_date_allowed=data['Date'].max()
        ),
    ]),

    # Plotly Chart
    dcc.Graph(id='stacked-bar-chart')
])


@app.callback(
    Output('stacked-bar-chart', 'figure'),
    [Input('start-date-picker', 'date'),
     Input('end-date-picker', 'date')]
)
def update_chart(start_date, end_date):
    filtered_data = data[(data['Date'] >= start_date) & (data['Date'] <= end_date)]

    fig = px.line(filtered_data, x='Date', y='Value', title="Date Range Chart", color_discrete_sequence=px.colors.qualitative.T10)

    return fig


if __name__ == '__main__':
    app.run_server(debug=True, port=8051)