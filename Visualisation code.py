# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 16:34:43 2025

@author: ropaf
"""

#importing all the functions necesssary
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#plotting graphs of different life expectancy at birth over the years
#defining a function i can repeatedly use to plot different countries within my df
#here it takes the dataframe, country, and a few customizations
def life_expectancy_plots(df, country, color, ls='-', label=None):
    #i want to filter by country and to make sure both sexes are represented
    country_data = df[(df['Location'] == country) & (df['Sex'] == 'Both sexes')]
    plt.plot(country_data['Year'], country_data['FactValueNumeric'], color=color, ls=ls, lw=3, label=label)
life_expectancy=pd.read_csv('life_expectancy_data.csv', index_col=0)
print(life_expectancy.columns)
#line plots to compare different countries
life_expectancy_plots(life_expectancy,'Zimbabwe', 'g', ls='--', label='Zimbabwe')
life_expectancy_plots(life_expectancy,'United Kingdom of Great Britain and Northern Ireland', 'b', ls='-', label='UK')
life_expectancy_plots(life_expectancy,'Canada', 'r', ls=':', label='Canada') 
life_expectancy_plots(life_expectancy,'Brazil', 'm', ls=':', label='Brazil') 
life_expectancy_plots(life_expectancy,'Indonesia', 'c', ls='-.', label='Indonesia')
plt.title('Life Expectancy in different countries over time')
plt.xlabel('Year')
plt.ylabel('Life Expectancy')
#my graph has a gap at the left so to correct this i'm using xlim on year
plt.xlim(left=life_expectancy['Year'].min()) 
plt.grid(True) #it looks better with gridlines
plt.legend()
plt.show()

#now we do a histogram to see how to distribute life expectancy in africa
#to filter my data set into the continent column only i'll use a function
def continent_data(df, region, color, bins=10, alpha=0.7, label=None):   
    region_data=df[(df['ParentLocation']==region)]
    plt.hist(region_data['FactValueNumeric'], bins=bins, alpha=alpha, label=label)
continent_data(life_expectancy, 'Africa', 'b', bins=10, alpha=0.9, label='Africa')
continent_data(life_expectancy, 'Europe', 'r', bins=10, alpha=0.5, label='Europe')
plt.xlabel('Life Expectancy')
plt.ylabel('Frequency')
plt.title('Distribution of Life Expectancy in Africa')
plt.legend()
plt.show()

#now to look at a third visualisation method
def continent_boxplots(df, continent):
    df.boxplot(column=continent, by='ParentLocation')
    plt.title('Boxplots by continent')
    plt.xlabel('Continent')
    plt.ylabel('Life Expectancy')
    plt.xticks(rotation=45)
continent_boxplots(life_expectancy, 'FactValueNumeric')
plt.show()       


