import codecademylib3_seaborn
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
df = pd.read_csv('WorldCupMatches.csv')
df_goals = pd.read_csv('goals.csv')
df['Total Goals'] = df['Home Team Goals']+ df['Away Team Goals']
#Figure1
fig1=plt.figure(figsize=(12,7))
ax1 = plt.subplots()
sns.set_style('whitegrid')
sns.set_context('poster', font_scale =0.5)
sns.barplot(data=df,y='Total Goals',x='Year')
plt.title('Avg Goals Scored')
plt.show()
#Figure2
fig = plt.figure(figsize =(12,7))
ax = plt.subplots()
sns.set_context('notebook',font_scale = 0.8)
sns.boxplot(data=df_goals,x='year',y='goals',palette ='Spectral')
plt.title('Goals Scored')
plt.show()
