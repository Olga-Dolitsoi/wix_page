import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go


excel_path = 'currency.xlsx'
df = pd.read_excel(excel_path)


def convert_to_datetime(date_str):
    date_str = str(date_str)
    # Split the string into month and year parts
    month_str, year_str = date_str.split('.')
    # Convert to integers
    month = int(month_str)
    year = int(year_str)
    # Create a datetime object
    return pd.to_datetime(f"{year}-{month:02d}-01")


# Apply the function to the DataFrame column
df['Date'] = df['Date'].apply(convert_to_datetime)

# Sample data

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Stacked Bar Chart with Date Range Picker"),

    # Date Range Picker
    html.Div([
        dcc.DatePickerSingle(
            id='start-date-picker',
            display_format='MM/YYYY',  # Display format for Month and Year
            date=df['Date'].min(),  # Start from January 2023
            min_date_allowed=df['Date'].min(),
            max_date_allowed=df['Date'].max()
        ),
        dcc.DatePickerSingle(
            id='end-date-picker',
            display_format='MM/YYYY',  # Display format for Month and Year
            date=df['Date'].max(),  # End at December 2023
            min_date_allowed=df['Date'].min(),
            max_date_allowed=df['Date'].max()
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
    filtered_data = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

    trace1 = go.Bar(x=filtered_data['Date'], y=filtered_data['Sell cash currency in equivalence'],
                    name='Sell cash currency in equivalence')
    trace2 = go.Bar(x=filtered_data['Date'], y=filtered_data['Sell cash USA currency'], name='Sell cash USA currency')
    trace3 = go.Bar(x=filtered_data['Date'], y=filtered_data['Sell non-cash currency'], name='Sell non-cash currency')
    trace4 = go.Bar(x=filtered_data['Date'], y=filtered_data['Sell non-cash currency USA'], name='Sell non-cash currency USA')
    trace5 = go.Bar(x=filtered_data['Date'], y=filtered_data['Summary'], name='Summary')

    data = [trace1, trace2, trace3, trace4, trace5]

    layout = go.Layout(barmode='relative', title="Stacked Bar Chart of Sales Data Over Time")

    fig = go.Figure(data=data, layout=layout)

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
