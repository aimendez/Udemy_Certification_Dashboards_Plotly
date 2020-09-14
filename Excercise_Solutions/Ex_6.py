#######################################################################################

# EXCERCISE 6: Histograms Excercise
# Udemy Online Course: "Python Visualization Dashboards with Plotly's Dash Library"
# https://www.udemy.com/course/interactive-python-dashboards-with-plotly-and-dash/

# @Author: AIMendez
# Created on 16-06-2020

#######################################################################################
# Objective: Create a histogram that plots the 'length' field
# from the Abalone dataset (../data/abalone.csv).
# Set the range from 0 to 1, with a bin size of 0.02
#######################################################################################

# Perform imports here:
import pandas as pd 
import plotly.offline as pyo
import plotly.graph_objs as go
import os
cwd = os.getcwd()

# create a DataFrame from the .csv file:
df = pd.read_csv( cwd+'/data/abalone.csv')

# create a data variable:

fig = go.Figure()

trace = go.Histogram( x = df.length ,
					  xbins = { 'start': 0, 
					  			'end': 1,
					  			'size':0.02
					  		   }
					)

fig.add_trace(trace)


# add a layout
layout = go.Layout( title = 'Excercise 6 Solution',
					xaxis_title = 'length' )
fig.update_layout(layout)


# create a fig from data & layout, and plot the fig
pyo.plot(fig, filename='Ex_6.html')
