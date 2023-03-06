# -*- coding: utf-8 -*-
"""Bar Graph.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NUKviymGieffp23SP-I6Y2BfIe478lU7
"""

#importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import plotly.express as px

#reading data
data = pd.read_csv('https://raw.githubusercontent.com/nethajinirmal13/Training-datasets/main/USA_Housing.csv') 
data

#Removing unwanted columns
data = data.drop(['Address','Avg. Area Income'],axis = 1)

data

#Checking the data types
data.dtypes

data = data.astype(int)

data['Avg. Area Number of Bedrooms'].unique()

#Checking how many bedrooms people prefferd
data['Avg. Area Number of Bedrooms'].value_counts()

data

#Plotting the data
data['Avg. Area Number of Bedrooms'].value_counts().plot(kind='bar',
                                    figsize=(14,8),
                                    title="Number of bedrooms people preferred the most", color=['green', 'blue', 'pink','orange','violet'])

