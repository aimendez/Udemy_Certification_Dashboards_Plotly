#######################################################################################

# EXCERCISE 7: Distplots Excercise
# Udemy Online Course: "Python Visualization Dashboards with Plotly's Dash Library"
# https://www.udemy.com/course/interactive-python-dashboards-with-plotly-and-dash/

# @Author: AIMendez
# Created on 16-06-2020

#######################################################################################
# Objective: Using the iris dataset, develop a Distplot
# that compares the petal lengths of each class.
# File: '../data/iris.csv'
# Fields: 'sepal_length','sepal_width','petal_length','petal_width','class'
# Classes: 'Iris-setosa','Iris-versicolor','Iris-virginica'
#######################################################################################


# Perform imports here:
import pandas as pd 
import plotly.offline as pyo
import plotly.graph_objs as go
import plotly.figure_factory as ff
import os
cwd = os.getcwd()


# create a DataFrame from the .csv file:
df = pd.read_csv( cwd + '/data/iris.csv')

# Define the traces

hist_data = [ df[df['class'] == label]['petal_length']  for label in df['class'].unique() ]
group_labels = df['class'].unique()



# Create a fig from data and layout, and plot the fig
fig = ff.create_distplot( hist_data ,
					       group_labels
					    )

layout = go.Layout( title = 'Excercise 7 Solution',
					xaxis_title = 'petal length' )
fig.update_layout(layout)

# create a fig from data & layout, and plot the fig
pyo.plot(fig, filename='Ex_7.html')
