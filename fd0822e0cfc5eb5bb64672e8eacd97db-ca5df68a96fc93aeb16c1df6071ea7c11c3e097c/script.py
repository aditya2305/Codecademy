import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn
import glob

states = glob.glob('states*')
state_list = []

for state in states:
  data = pd.read_csv(state)
  state_list.append(data)
us_census = pd.concat(state_list).reset_index()
#print(us_census)
print(us_census.dtypes)
print(us_census.dtypes.head())
#Removing $ from income column using reqex
us_census.Income = us_census.Income.replace('[\$]','',regex=True)
#print(us_census)
#Seperating GenderPop column into two columns
Men_women = us_census.GenderPop.str.split("_",expand = True)
us_census['Men'] = Men_women.get(0)
us_census['Women'] = Men_women.get(1)
#Removing 'M' and 'F' from Men and Women columns
us_census.Men = us_census.Men.replace('[M]','',regex=True)
us_census.Women = us_census.Women.replace('[F]','',regex=True)
#Dropping unnecessary columns
us_census=us_census.drop(['GenderPop','Unnamed: 0'],axis=1)
#Convert columns to float
us_census.Men = pd.to_numeric(us_census.Men)
us_census.Women = pd.to_numeric(us_census.Women)
us_census.Income = pd.to_numeric(us_census.Income)
#Fill nan values
us_census.Women = us_census.Women.fillna(us_census.TotalPop-us_census.Men)
#Drop duplicate states
us_census.State=us_census.State.drop_duplicates()
#Scatter Plot
plt.scatter(us_census.Women,us_census.Income)
plt.show()
print(us_census)