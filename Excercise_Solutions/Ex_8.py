#######################################################################################

# EXCERCISE 8: Heatmaps Excercise
# Udemy Online Course: "Python Visualization Dashboards with Plotly's Dash Library"
# https://www.udemy.com/course/interactive-python-dashboards-with-plotly-and-dash/

# @Author: AIMendez
# Created on 16-06-2020

#######################################################################################
# Objective: Using the "flights" dataset available
# from the data folder as flights.csv
# create a heatmap with the following parameters:
# x-axis="year"
# y-axis="month"
# z-axis(color)="passengers"
#######################################################################################

# Perform imports here:
import pandas as pd 
import plotly.offline as pyo
import plotly.graph_objs as go
import os
cwd = os.getcwd()


# Create a DataFrame from  "flights" data
df = pd.read_csv( cwd+'/data/flights.csv')

# Define a data variable
fig = go.Figure()

trace = go.Heatmap( x = df.year ,
					y = df.month,
					z = df.passengers.values.tolist(),
					zmin = 0,
					zmax = df.passengers.max()

					)

fig.add_trace(trace)

# Define the layout
layout = go.Layout( title = 'Excercise 8 Solution',
					xaxis_title = 'year',
					yaxis_title = 'month',
				   )
fig.update_layout(layout)

# create a fig from data & layout, and plot the fig
pyo.plot(fig, filename='Ex_8.html')
