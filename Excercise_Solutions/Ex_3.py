#######################################################################################

# EXCERCISE 3: Bar Chart Excercise
# Udemy Online Course: "Python Visualization Dashboards with Plotly's Dash Library"
# https://www.udemy.com/course/interactive-python-dashboards-with-plotly-and-dash/

# @Author: AIMendez
# Created on 16-06-2020

#######################################################################################

# Objective: Create a stacked bar chart from
# the file ../data/mocksurvey.csv. Note that questions appear in
# the index (and should be used for the x-axis), while responses
# appear as column labels.  Extra Credit: make a horizontal bar chart!

#######################################################################################


# Perform imports here:
import pandas as pd 
import plotly.offline as pyo
import plotly.graph_objs as go
import os
cwd = os.getcwd()

# create a DataFrame from the .csv file:
df = pd.read_csv( cwd+'/data/mocksurvey.csv', index_col = 0 )

# create traces using a list comprehension:
fig = go.Figure()

traces = [go.Bar(
	  			x = df.index,
			    y = df[response],
			    name=response
				) for response in df.columns]

fig.add_traces(traces)

# create a layout, remember to set the barmode here
layout = go.Layout(
    title='Excercise 3 Solution',
    barmode='stack'
)

fig.update_layout(layout)

# create a fig from data & layout, and plot the fig.
pyo.plot(fig, filename='Ex_3.html')
