# -*- coding: utf-8 -*-
"""
Created on Fri May 11 12:08:42 2018

@author: aniketsha
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tips = pd.read_csv('tips.csv')

# Distplot is used to plot the distribution of the any single column.
sns.distplot(tips['total_bill'])
sns.distplot(tips['total_bill'],kde=False)

# Jointplot is used to compare between the two columns.
sns.jointplot(x=tips['total_bill'],y=tips['tip'], data=tips)
sns.jointplot(x=tips['total_bill'],y=tips['tip'], data=tips,kind='hex')
sns.jointplot(x=tips['total_bill'],y=tips['tip'], data=tips,kind='reg')
sns.jointplot(x=tips['total_bill'],y=tips['tip'], data=tips,kind='kde')

# Pairplot is used to plot each column of df to each other column of df which has numerical datatype
sns.pairplot(tips)
# usig hue parameter we can add categorical variable whcih reflects in graph
sns.pairplot(tips, hue='sex')

# Rugplot is similar distplot but in rugplot the bars are converted to vertical consecutives lines..more the value dense will be the rugplot ie it draws a single vertcle line for every record in dataset
sns.rugplot(tips['total_bill'])

# Categorical data

#Bar plot it is used to plot the categorical data after averaging out the values against the numerical value.(groupby action)
sns.barplot(x=tips['sex'],y=tips['total_bill'],data=tips)
import numpy as np
sns.barplot(x=tips['sex'],y=tips['total_bill'],data=tips, estimator=np.std)

#Countplot is used to count the frequency of the categorical variable
sns.countplot(x='sex',data=tips)

#Box plot is used to show the distribution of the categorical values and show th outliers and range of values.
sns.boxplot(x=tips['day'],y=tips['total_bill'],data=tips)

sns.boxplot(x=tips['day'],y=tips['total_bill'],data=tips,hue='sex')

#Violin plot is similar to box plot
sns.violinplot(x=tips['day'],y=tips['total_bill'],data=tips)
sns.violinplot(x=tips['day'],y=tips['total_bill'],data=tips,hue='sex',split=True)

# Stripplot is same like box plot bt it uses scatter plot to show the frequency
sns.stripplot(x=tips['day'],y=tips['total_bill'],data=tips)
# to get more clear view jitter property is used
sns.stripplot(x=tips['day'],y=tips['total_bill'],data=tips,jitter=True)
sns.stripplot(x=tips['day'],y=tips['total_bill'],data=tips,jitter=True,hue='sex',split=True)

#Heatmap
flights = pd.read_csv('flights.csv')
pt = flights.pivot_table(index='month',columns='year',values='passengers')
un = pt.unstack(level=-1)
sns.heatmap(pt)
sns.heatmap(pt, cmap='magma')
sns.heatmap(pt, cmap='coolwarm', linecolor='white',linewidths=1)
sns.heatmap(pt, cmap='coolwarm', linecolor='black',linewidths=1)

#cluster map, similar groups are closer to each other
sns.clustermap(pt,cmap='coolwarm')

#Regression plots used mainly for linear model representations

sns.lmplot(x='total_bill',y='tip',data=tips)
sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex')
sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex',markers=['o','v'])

# Style and color
sns.set_style(style='darkgrid')
# sns.set_style(style='whitegrid')
# sns.set_style(style='white')
sns.countplot(x='sex',data=tips)

plt.figure(figsize=(12,3))
sns.countplot(x='sex',data=tips)

sns.set_context(context='poster')
sns.countplot(x='sex',data=tips)

sns.set_context(context='notebook')
sns.countplot(x='sex',data=tips)

sns.set_context(context='talk')
sns.countplot(x='sex',data=tips)
