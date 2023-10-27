import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import dash_mantine_components as dmc
import datetime
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
        dmc.Group(
            spacing="xl",
            children=[
                dmc.DatePicker(
                    id='start-date-picker',
                    label="Start Date",
                    inputFormat='MM/YYYY',  # Display format for Month and Year
                    value=df['Date'].min(),  # Start from January 2023
                    minDate=df['Date'].min(),
                    maxDate=df['Date'].max()+datetime.timedelta(hours=12),
                    #allowLevelChange=False,
                    initialLevel='month',
                    style={"width": 200}
                ),
                dmc.DatePicker(
                    id='end-date-picker',
                    label="End Date",
                    inputFormat='MM/YYYY',  # Display format for Month and Year
                    value=df['Date'].max(),  # End at December 2023
                    minDate=df['Date'].min(),
                    maxDate=df['Date'].max()+datetime.timedelta(hours=12),
                    #allowLevelChange=False,
                    initialLevel='month',
                    style={"width": 200}
                ),
            ]
        )
    ]),

    # Plotly Chart
    dcc.Graph(id='stacked-bar-chart',
              style={'width': '190vh', 'height': '90vh'}
              )
])

@app.callback(
    Output('stacked-bar-chart', 'figure'),
    [Input('start-date-picker', 'value'),
     Input('end-date-picker', 'value')]
)
def update_chart(start_date, end_date):
    filtered_data = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
    colours = {'Buy of non-cash currency': "#B7D9E6",
               'Buy of cash currency': "#94C7DA",
               'Sell of cash currency': "#ADD38B",
               'Sell of non-cash currency': "#C9E1B3"}

    trace1 = px.bar(filtered_data,
                    x='Date',
                    y=['Sell of cash currency',
                       'Buy of cash currency',
                       'Buy of non-cash currency',
                       'Sell of non-cash currency'],
                    color_discrete_map=colours
                    )

    trace5 = px.line(filtered_data, x='Date', y='Summary', markers=True)\
        .update_traces(showlegend=True, line_color="#991C1F", name="Summary")

    #data = [trace1, trace2, trace3, trace4, trace5]

    #layout = go.Layout(barmode='stack', title="Stacked Bar Chart of Sales Data Over Time")

    fig = go.Figure(data=trace1.data + trace5.data)
    fig.update_layout(barmode='relative', font_size=20)

    return fig


if __name__ == '__main__':
    app.run_server(debug=True, port=8052)
