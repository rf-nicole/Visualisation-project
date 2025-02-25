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
def life_expectancy_plots(df, country, color, ls='-', label=None):
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

#now we do a scatter plot to try see if there is a correlation
region_data=life_expectancy[life_expectancy['ParentLocation']=='Africa']
plt.hist(region_data['FactValueNumeric'], bins=10,color='b', alpha=0.7)
plt.xlabel('Life Expectancy')
plt.ylabel('Frequency')
plt.title('Distribution of Life Expectancy in Africa')
plt.show()


