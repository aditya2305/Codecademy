import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import matplotlib.ticker as mtick

df = pd.read_csv('kiva_data.csv')
print(df.head())
fig = plt.figure(figsize=(15,10))
ax= plt.subplot()
sns.barplot(data=df, x='country', y='loan_amount',hue='activity')
sns.set_palette('Dark2')
sns.set_style('dark')
fmt = '${x:,.0f}'
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)
plt.title('Loan Given To Countries')
plt.show()

fig2 = plt.figure(figsize=(16,10))
ax2 = plt.subplot()
sns.boxplot(data=df,x='country',y='loan_amount')
plt.show()

fig3 = plt.figure(figsize=(16,10))
ax3 = plt.subplot()
sns.violinplot(x='country',data=df,y='loan_amount')
plt.show()

fig4 = plt.figure(figsize=(16,10))
ax4 = plt.subplot()
sns.violinplot(data=df,x='country',y='loan_amount',hue='gender',split=True)
plt.show()

