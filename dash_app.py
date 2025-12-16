#!/usr/bin/env python
# coding: utf-8

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Load the data
data = pd.read_csv(
    'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv'
)

# Initialize the Dash app
app = dash.Dash(__name__)
app.title = "Automobile Statistics Dashboard"  # TASK 2.1

# Dropdown options
dropdown_options = [
    {'label': 'Yearly Statistics', 'value': 'Yearly Statistics'},
    {'label': 'Recession Period Statistics', 'value': 'Recession Statistics'}
]

# List of years
year_list = [i for i in range(1980, 2024)]

# Layout
app.layout = html.Div([
    # TASK 2.1: Title
    html.H1("Automobile Statistics Dashboard", style={'textAlign': 'center', 'color': 'darkblue'}),
    
    # TASK 2.2: Dropdowns
    html.Div([
        html.Label("Select Statistics:"),
        dcc.Dropdown(
            id='statistic-dropdown',
            options=dropdown_options,
            value='Yearly Statistics',
            placeholder='Select statistics type'
        )
    ], style={'width': '40%', 'margin': '10px'}),
    
    html.Div([
        html.Label("Select Year:"),
        dcc.Dropdown(
            id='select-year',
            options=[{'label': i, 'value': i} for i in year_list],
            value=2023
        )
    ], style={'width': '20%', 'margin': '10px'}),
    
    # TASK 2.3: Output division
    html.Div(id='output-container', className='output-container', style={'marginTop': '20px'})
])

# TASK 2.4: Callback to enable/disable year selection
@app.callback(
    Output('select-year', 'disabled'),
    Input('statistic-dropdown', 'value')
)
def update_year_dropdown(selected_statistics):
    if selected_statistics == 'Yearly Statistics':
        return False
    return True

# TASK 2.5 & 2.6: Main plotting callback
@app.callback(
    Output('output-container', 'children'),
    [Input('statistic-dropdown', 'value'), Input('select-year', 'value')]
)
def update_output_container(selected_statistics, input_year):
    
    if selected_statistics == 'Recession Statistics':
        recession_data = data[data['Recession'] == 1]

        # Plot 1: Yearly sales during recession
        yearly_rec = recession_data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        R_chart1 = dcc.Graph(
            figure=px.line(yearly_rec, x='Year', y='Automobile_Sales',
                           title="Average Automobile Sales Fluctuation over Recession Period")
        )

        # Plot 2: Average vehicles sold by type
        average_sales = recession_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()
        R_chart2 = dcc.Graph(
            figure=px.bar(average_sales, x='Vehicle_Type', y='Automobile_Sales',
                          title="Average Vehicles Sold by Vehicle Type during Recession")
        )

        # Plot 3: Pie chart of advertising expenditure
        exp_rec = recession_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum().reset_index()
        R_chart3 = dcc.Graph(
            figure=px.pie(exp_rec, names='Vehicle_Type', values='Advertising_Expenditure',
                          title="Advertising Expenditure Share by Vehicle Type during Recession")
        )

        # Plot 4: Unemployment vs vehicle sales
        unemp_data = recession_data.groupby(['unemployment_rate', 'Vehicle_Type'])['Automobile_Sales'].mean().reset_index()
        R_chart4 = dcc.Graph(
            figure=px.bar(unemp_data, x='unemployment_rate', y='Automobile_Sales', color='Vehicle_Type',
                          labels={'unemployment_rate': 'Unemployment Rate', 'Automobile_Sales': 'Average Automobile Sales'},
                          title='Effect of Unemployment Rate on Vehicle Type and Sales')
        )

        return [
            html.Div([R_chart1, R_chart2], style={'display': 'flex'}),
            html.Div([R_chart3, R_chart4], style={'display': 'flex'})
        ]

    elif selected_statistics == 'Yearly Statistics' and input_year:
        yearly_data = data[data['Year'] == input_year]

        # Plot 1: Yearly Automobile Sales (line chart)
        yas = data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        Y_chart1 = dcc.Graph(
            figure=px.line(yas, x='Year', y='Automobile_Sales', title='Yearly Automobile Sales')
        )

        # Plot 2: Total Monthly Automobile Sales
        mas = yearly_data.groupby('Month')['Automobile_Sales'].sum().reset_index()
        Y_chart2 = dcc.Graph(
            figure=px.line(mas, x='Month', y='Automobile_Sales', title=f'Total Monthly Automobile Sales ({input_year})')
        )

        # Plot 3: Average Vehicles Sold by Vehicle Type
        avr_vdata = yearly_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()
        Y_chart3 = dcc.Graph(
            figure=px.bar(avr_vdata, x='Vehicle_Type', y='Automobile_Sales',
                          title=f'Average Vehicles Sold by Vehicle Type in {input_year}')
        )

        # Plot 4: Total Advertising Expenditure by Vehicle Type
        exp_data = yearly_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum().reset_index()
        Y_chart4 = dcc.Graph(
            figure=px.pie(exp_data, names='Vehicle_Type', values='Advertising_Expenditure',
                          title=f'Advertising Expenditure Share by Vehicle Type in {input_year}')
        )

        return [
            html.Div([Y_chart1, Y_chart2], style={'display': 'flex'}),
            html.Div([Y_chart3, Y_chart4], style={'display': 'flex'})
        ]

    else:
        return None

# Run the Dash app
if __name__ == '__main__':
    app.run(debug=True)
