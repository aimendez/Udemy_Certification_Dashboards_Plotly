#######################################################################################

# EXCERCISE 5: Boxplots Excercise
# Udemy Online Course: "Python Visualization Dashboards with Plotly's Dash Library"
# https://www.udemy.com/course/interactive-python-dashboards-with-plotly-and-dash/

# @Author: AIMendez
# Created on 16-06-2020

#######################################################################################
# Objective: Make a DataFrame using the Abalone dataset (../data/abalone.csv).
# Take two independent random samples of different sizes from the 'rings' field.
# HINT: np.random.choice(df['rings'],10,replace=False) takes 10 random values
# Use box plots to show that the samples do derive from the same population.
#######################################################################################

# Perform imports here:
import pandas as pd 
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go
import os
cwd = os.getcwd()

# create a DataFrame from the .csv file:
df = pd.read_csv( cwd+'/data/abalone.csv')
print(df.head())

# take two random samples of different sizes:

sample_0 = np.random.choice(df['rings'],10,replace=False)
sample_1 = np.random.choice(df['rings'],10,replace=False)


# create a data variable with two Box plots:
fig = go.Figure()

trace0 = go.Box(
			    y = sample_0,
			    boxpoints = 'all', #'outliers' as second option
			    jitter = 0.1, #how spread the points are
			    pointpos = 0 #off set of points respect to box
			  )

trace1 = go.Box(
			    y = sample_1,
			    boxpoints = 'all', 
			    jitter = 0.3,
			    pointpos = 0
			  )
		

fig.add_traces([trace0, trace1])


# add a layout
layout = go.Layout(
				    title = 'Excercise 5 Solution',
				    xaxis_title = 'rings',
					)

fig.update_layout(layout)


# create a fig from data & layout, and plot the fig
pyo.plot(fig, filename='Ex_5.html')
