# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 16:34:43 2025

@author: ropaf
"""

#importing all the functions necesssary
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

life_expectancy=pd.read_csv('life_expectancy_data.csv', index_col=0)
print(life_expectancy.columns)
#i want a line plot to see how the life expectancy in african countries has improved through the years
country_AFR=life_expectancy[(life_expectancy['Location']=='Zimbabwe') & (life_expectancy['Sex']=='Both sexes')]
#sorting my data by year
country_AFR=country_AFR.sort_values(by='Year') 
plt.plot(country_AFR['Year'],country_AFR['FactValueNumeric'])
plt.title('Life Expectancy in Zimbabwe Over Time')
plt.xlabel('Year')
plt.ylabel('Life Expectancy')
plt.show()




