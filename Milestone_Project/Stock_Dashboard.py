#######################################################################################

# Milestone Project: Stock Price Dashboard 
# Udemy Online Course: "Python Visualization Dashboards with Plotly's Dash Library"
# https://www.udemy.com/course/interactive-python-dashboards-with-plotly-and-dash/

# @Author: AIMendez
# Created on 16-06-2020

#######################################################################################
import dash
import dash_core_components as dcc 
import dash_html_components as html 
import dash_bootstrap_components as dbc 
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import pandas as pd 
import pandas_datareader.data as web
from pandas_datareader.nasdaq_trader import get_nasdaq_symbols
from datetime import datetime
import os
os.environ["IEX_API_KEY"] = "pk_514308cb395240bdab944461ab1b3360"


symbols = get_nasdaq_symbols().index.tolist()
symbols = [{'label': symbol , 'value': symbol}   for symbol in symbols]
dropdown_menu = dcc.Dropdown(
							id = 'dropdown',
							options = symbols,
							placeholder = 'Select a symbol',
							value = 'AAPL',
							)


calendar = dcc.DatePickerRange(
	        id='calendar',
	        min_date_allowed= datetime(2000, 8, 5),
	        max_date_allowed= datetime.today(),
	        initial_visible_month=datetime(2017, 8, 5),
	        start_date = datetime(2018, 1, 1),
	        end_date= datetime.today()
	    )



app = dash.Dash(__name__, external_stylesheets = [dbc.themes.BOOTSTRAP])

app.layout = html.Div([ dbc.Row([ html.H1('Milestone Project - Stock Ticker Dashboard')]),
						dbc.Row([
								dbc.Col([
										html.P(),
										html.H4('Select Stock Symbol'),
										dropdown_menu ,
										html.P('\n', style = {'marginBottom':30}),
										], width = {'size':2}),
								dbc.Col([
										html.P(),
										html.H4('Select Start and End Dates'),
										calendar ,
										html.P('\n', style = {'marginBottom':30}),
										], width = {'size':2}),
								#dbc.Col([
								#		html.P(),
								#		submit_button], width = {'size':2})
								]),

						dbc.Row([ 
								dcc.Graph(id = 'ohlc_plot')
								])
						], style = {'marginLeft':50})



@app.callback( Output('ohlc_plot', 'figure'),
			  [Input('dropdown', 'value'),
			   Input('calendar', 'start_date'),
			   Input('calendar', 'end_date')]
			 )

def candlestick_chart(SYMBOL, start, end):
	df = web.DataReader( SYMBOL, 'iex', start, end )
	fig = go.Figure()
	trace = go.Candlestick( x = df.index ,
							open = df.open,
							high = df.high,
							low = df.low,
							close = df.close)

	layout = go.Layout( title = SYMBOL + ' - Candlestick Chart',
						xaxis = {'title' : 'Date', 'showgrid':False, 'type':'category'},
						yaxis = {'title': 'Price', 'showgrid':False},
						xaxis_rangeslider_visible = False,
						plot_bgcolor = '#FFFFFF'
					)

	fig.add_trace(trace)
	fig.update_layout(layout)
	return fig 

###########################################################################################
if __name__ == '__main__':
	app.run_server()




















