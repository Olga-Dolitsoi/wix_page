import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import datetime
import plotly.express as px
import plotly.graph_objects as go
import gc


class StackedBarChartApp:
    def __init__(self):
        self.app = dash.Dash(__name__)

        self.df = pd.read_excel('currency.xlsx')  # Define your DataFrame here

        def convert_to_datetime(date_str):
            date_str = str(date_str)
            # Split the string into month and year parts
            month_str, year_str = date_str.split('.')
            # Convert to integers
            month = int(month_str)
            year = int(year_str)
            # Create a datetime object
            return pd.to_datetime(f"{year}-{month:02d}-01")

        self.df['Date'] = self.df['Date'].apply(convert_to_datetime)
        self.app.layout = html.Div([
            html.H1("Stacked Bar Chart with Date Range Picker"),

            # Date Range Picker
            html.Div([
                dcc.DatePickerSingle(
                    id='start-date-picker',
                    display_format='MM/YYYY',  # Display format for Month and Year
                    date=self.df['Date'].min(),  # Start from January 2023
                    min_date_allowed=self.df['Date'].min(),
                    max_date_allowed=self.df['Date'].max() + datetime.timedelta(hours=12),
                    initial_visible_month=self.df['Date'].min(),
                ),
                dcc.DatePickerSingle(
                    id='end-date-picker',
                    display_format='MM/YYYY',  # Display format for Month and Year
                    date=self.df['Date'].max(),  # End at December 2023
                    min_date_allowed=self.df['Date'].min(),
                    max_date_allowed=self.df['Date'].max() + datetime.timedelta(hours=12),
                    initial_visible_month=self.df['Date'].max(),
                ),
            ]),

            # Plotly Chart
            dcc.Graph(id='stacked-bar-chart',
                      style={'width': '190vh', 'height': '90vh'}
                      )
        ])

        @self.app.callback(
            Output('stacked-bar-chart', 'figure'),
            [Input('start-date-picker', 'date'),
             Input('end-date-picker', 'date')]
        )
        def update_chart(start_date, end_date):

            filtered_data = self.df[(self.df['Date'] >= start_date) & (self.df['Date'] <= end_date)]
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

            trace5 = px.line(filtered_data, x='Date', y='Summary', markers=True) \
                .update_traces(showlegend=True, line_color="#991C1F", name="Summary")

            # data = [trace1, trace2, trace3, trace4, trace5]

            # layout = go.Layout(barmode='stack', title="Stacked Bar Chart of Sales Data Over Time")

            fig = go.Figure(data=trace1.data + trace5.data)
            fig.update_layout(barmode='relative', font_size=20)

            return fig

    def run_app(self):
        if __name__ == '__main__':
            self.app.run_server(debug=True, host='0.0.0.0', port=8057)


if __name__ == '__main__':
    app = StackedBarChartApp()
    app.run_app()
    gc.collect()


