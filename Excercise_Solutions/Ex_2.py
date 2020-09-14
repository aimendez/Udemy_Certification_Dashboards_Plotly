#######################################################################################

# EXCERCISE 2: Line Charts Excercise
# Udemy Online Course: "Python Visualization Dashboards with Plotly's Dash Library"
# https://www.udemy.com/course/interactive-python-dashboards-with-plotly-and-dash/

# @Author: AIMendez
# Created on 16-06-2020

#######################################################################################

# Objective: Using the file 2010YumaAZ.csv, develop a Line Chart
# that plots seven days worth of temperature data on one graph.
# You can use a for loop to assign each day to its own trace.

#######################################################################################

# Perform imports here:
import pandas as pd 
import plotly.offline as pyo
import plotly.graph_objs as go
import os
cwd = os.getcwd()

# Create a pandas DataFrame from 2010YumaAZ.csv
df = pd.read_csv( cwd+'/data/2010YumaAZ.csv')
days = ['TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY','MONDAY']


# Use a for loop (or list comprehension to create traces for the data list)
fig = go.Figure()

for day in days:
	trace = go.Scatter( x = df[ df.DAY == day].LST_TIME,
					    y =  df[ df.DAY == day].T_HR_AVG,
					    name = day
					  )
	fig.add_traces(trace)

# Define the layout
layout = go.Layout(
    				title='Excercise 2 Solution'
				  )

fig.update_layout(layout)

# Create a fig from data and layout, and plot the fig
pyo.plot(fig, filename='Ex_2.html')
