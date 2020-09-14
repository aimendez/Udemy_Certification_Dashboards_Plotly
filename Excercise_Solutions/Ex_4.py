#######################################################################################

# EXCERCISE 4: Bubble Chart Excercise
# Udemy Online Course: "Python Visualization Dashboards with Plotly's Dash Library"
# https://www.udemy.com/course/interactive-python-dashboards-with-plotly-and-dash/

# @Author: AIMendez
# Created on 16-06-2020

#######################################################################################

# Objective: Create a bubble chart that compares three other features
# from the mpg.csv dataset. Fields include: 'mpg', 'cylinders', 'displacement'
# 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'name'

#######################################################################################


# Perform imports here:
import pandas as pd 
import plotly.offline as pyo
import plotly.graph_objs as go
import os
cwd = os.getcwd()



# create a DataFrame from the .csv file:
df = pd.read_csv( cwd+'/data/mpg.csv')

# create data by choosing fields for x, y and marker size attributes

fig = go.Figure()

trace = go.Scatter(
	  			x = df.weight,
			    y = df.mpg,
			    text = df.name,
			    mode = 'markers',
			    marker = {'size':df.acceleration, 
			    		  'color':df.cylinders }
			    		  )
		

fig.add_traces(trace)



# create a layout with a title and axis labels
layout = go.Layout(
				    title = 'Excercise 4 Solution',
				    xaxis_title = 'Weight',
				    yaxis_title = 'MPG'
					)

fig.update_layout(layout)


# create a fig from data & layout, and plot the fig
pyo.plot(fig, filename='Ex_4.html')
